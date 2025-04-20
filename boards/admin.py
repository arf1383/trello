from django.contrib import admin
from .models import Board, Task, Status, Label

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'assigned_to', 'board')
    list_filter = ('status', 'labels', 'board')
    search_fields = ('title',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    search_fields = ('name',)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    search_fields = ('name',)
