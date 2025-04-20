from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'statuses', views.StatusViewSet)
router.register(r'labels', views.LabelViewSet)

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:board_id>/tasks/', views.task_list, name='task_list'),
    path('reports/monthly/', views.monthly_work_report, name='monthly_report'),
    path('reports/daily/', views.daily_task_report, name='daily_report'),
    path('api/', include(router.urls)),
]
