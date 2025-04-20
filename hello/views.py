import re
from django.utils.timezone import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from hello.forms import LogMessageForm
from hello.models import LogMessage, Workspace, Board, Task, WorkspaceMembership
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

User = get_user_model()

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")


@login_required
def log_message(request):
    form = LogMessageForm(request.POST or None)
    workspaces = Workspace.objects.filter(members=request.user)
    users = User.objects.all()

    if request.method == "POST":
        message_type = request.POST.get("message_type")
        if message_type == "group":
            if form.is_valid():
                message = form.save(commit=False)
                message.log_date = datetime.now()
                message.save()
                return redirect("home")
        elif message_type == "task":
            workspace_id = request.POST.get("workspace")
            user_id = request.POST.get("user")
            task_message = request.POST.get("task_message")
            try:
                workspace = Workspace.objects.get(id=workspace_id, members=request.user)
                user = User.objects.get(id=user_id)
                Task.objects.create(
                    title="Task from message",
                    description=task_message,
                    board=workspace.boards.first(),  # Assuming the first board is used
                    assigned_to=user
                )
                return redirect("home")
            except (Workspace.DoesNotExist, User.DoesNotExist):
                return JsonResponse({"error": "Invalid workspace or user."}, status=400)

    return render(request, "hello/log_message.html", {"form": form, "workspaces": workspaces, "users": users})


@login_required
def create_workspace(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        workspace = Workspace.objects.create(name=name, description=description)
        workspace.members.add(request.user)
        return JsonResponse({"message": "Workspace created successfully!"})
    return render(request, "hello/create_workspace.html")


@login_required
def invite_to_workspace(request, workspace_id):
    """Invite a user to the workspace and assign a role."""
    workspace = get_object_or_404(Workspace, id=workspace_id, members=request.user)
    if request.method == "POST":
        username = request.POST.get("username")
        role = request.POST.get("role", "Member")
        try:
            user = User.objects.get(username=username)
            membership, created = WorkspaceMembership.objects.get_or_create(user=user, workspace=workspace)
            membership.role = role
            membership.save()
            return JsonResponse({"message": f"User {username} added to workspace successfully with role {role}!"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
    return render(request, "hello/invite_to_workspace.html", {"workspace_id": workspace_id})


@login_required
def create_board(request, workspace_id):
    if request.method == "POST":
        name = request.POST.get("name")
        workspace = Workspace.objects.get(id=workspace_id)
        board = Board.objects.create(name=name, workspace=workspace)
        return JsonResponse({"message": "Board created successfully!"})
    return render(request, "hello/create_board.html", {"workspace_id": workspace_id})


@login_required
def create_task(request, board_id):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        assigned_to_username = request.POST.get("assigned_to")
        board = Board.objects.get(id=board_id)
        assigned_to = User.objects.filter(username=assigned_to_username).first()
        Task.objects.create(title=title, description=description, board=board, assigned_to=assigned_to)
        return JsonResponse({"message": "Task created successfully!"})
    return render(request, "hello/create_task.html", {"board_id": board_id})


@login_required
def list_workspaces(request):
    """List all workspaces the user is a member of."""
    workspaces = Workspace.objects.filter(members=request.user)
    return render(request, "hello/list_workspaces.html", {"workspaces": workspaces})

@login_required
def add_team_member(request, workspace_id):
    """Allow workspace owners to add team members."""
    workspace = get_object_or_404(Workspace, id=workspace_id, members=request.user)
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            if user not in workspace.members.all():
                workspace.members.add(user)
                return JsonResponse({"message": f"User {username} added to workspace successfully!"})
            else:
                return JsonResponse({"error": "User is already a member of this workspace."}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
    return render(request, "hello/add_team_member.html", {"workspace": workspace})


@login_required
def workspace_detail(request, workspace_id):
    """View to display workspace details, members, roles, and their tasks."""
    workspace = get_object_or_404(Workspace, id=workspace_id, members=request.user)
    memberships = WorkspaceMembership.objects.filter(workspace=workspace).select_related('user')
    member_tasks = {
        membership.user: Task.objects.filter(assigned_to=membership.user, board__workspace=workspace)
        for membership in memberships
    }

    context = {
        'workspace': workspace,
        'memberships': memberships,
        'member_tasks': member_tasks,
    }
    return render(request, 'hello/workspace_detail.html', context)


@login_required
def assign_task_and_role(request, workspace_id):
    """Allow workspace owners to assign tasks and roles to team members."""
    workspace = get_object_or_404(Workspace, id=workspace_id, members=request.user)
    if not WorkspaceMembership.objects.filter(workspace=workspace, user=request.user, role="Admin").exists():
        raise PermissionDenied("Only Admins can assign tasks and roles.")

    if request.method == "POST":
        username = request.POST.get("username")
        task_id = request.POST.get("task_id")
        role = request.POST.get("role")

        try:
            user = User.objects.get(username=username)
            membership = WorkspaceMembership.objects.get(user=user, workspace=workspace)
            membership.role = role
            membership.save()

            if task_id:
                task = Task.objects.get(id=task_id, board__workspace=workspace)
                task.assigned_to = user
                task.save()

            return JsonResponse({"message": f"Task assigned to {username} and role updated to {role}."})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found."}, status=404)
        except WorkspaceMembership.DoesNotExist:
            return JsonResponse({"error": "User is not a member of this workspace."}, status=404)

    tasks = Task.objects.filter(board__workspace=workspace)
    memberships = WorkspaceMembership.objects.filter(workspace=workspace).select_related('user')
    return render(request, "hello/assign_task_and_role.html", {"workspace": workspace, "tasks": tasks, "memberships": memberships})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "hello/register.html", {"form": form})


class LogoutAllowGetView(LogoutView):
    def get(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().post(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "hello/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Welcome, {self.request.user.username}!")
        return response
