from django.contrib import admin
from .models import Workspace, Board, Task

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("name", "workspace", "created_at")
    search_fields = ("name", "workspace__name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "board", "assigned_to", "completed", "created_at")
    search_fields = ("title", "board__name", "assigned_to__username")
