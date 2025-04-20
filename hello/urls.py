from django.urls import path
from hello import views
from hello.models import LogMessage
from django.contrib.auth import views as auth_views
from hello.views import LogoutAllowGetView, CustomLoginView

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    path("workspace/create/", views.create_workspace, name="create_workspace"),
    path("workspace/<int:workspace_id>/invite/", views.invite_to_workspace, name="invite_to_workspace"),
    path("workspace/<int:workspace_id>/board/create/", views.create_board, name="create_board"),
    path("workspace/<int:workspace_id>/detail/", views.workspace_detail, name="workspace_detail"),
    path("board/<int:board_id>/task/create/", views.create_task, name="create_task"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutAllowGetView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("workspaces/", views.list_workspaces, name="list_workspaces"),
    path("workspace/<int:workspace_id>/add-member/", views.add_team_member, name="add_team_member"),
    path("workspace/<int:workspace_id>/assign-task-role/", views.assign_task_and_role, name="assign_task_and_role"),
]

