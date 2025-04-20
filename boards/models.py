from django.db import models
from django.conf import settings

class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    due_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    labels = models.ManyToManyField(Label, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards', null=True, blank=True)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
