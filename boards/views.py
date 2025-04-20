from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Board, Task, Status, Label
from django.db.models import Count, Sum
from django.utils.timezone import now
from rest_framework import generics, viewsets, permissions
from .serializers import BoardSerializer, TaskSerializer, StatusSerializer, LabelSerializer
from .permissions import IsBoardAdmin

User = get_user_model()

class BoardListCreateView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

def board_list(request):
    boards = Board.objects.all()
    return render(request, 'boards/board_list.html', {'boards': boards})

def task_list(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    tasks = board.tasks.all()
    return render(request, 'boards/task_list.html', {'board': board, 'tasks': tasks})

def monthly_work_report(request):
    current_month = now().month
    tasks = Task.objects.filter(
        status__name='Done',
        end_date__month=current_month
    ).aggregate(total_hours=Sum('end_date'))
    return render(request, 'boards/monthly_report.html', {'tasks': tasks})

def daily_task_report(request):
    today = now().date()
    tasks = Task.objects.filter(
        status__name='Done',
        end_date=today
    ).count()
    return render(request, 'boards/daily_report.html', {'tasks': tasks})

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated, IsBoardAdmin]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsBoardAdmin]

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]
# Removed HTML template code. Ensure it is moved to a separate file, e.g., "boards/templates/boards/kanban_board.html".
