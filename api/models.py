from django.db import models

# Create your models here.


class Completed(models.Model):
    """Save todo state as completed or not"""

    completed = models.BooleanField(default=False)


class Todo(models.Model):
    """Save todo"""

    title: models = models.CharField(max_length=200, name="todo_title")
    body: models = models.CharField(max_length=3000, name="todo_body")
    completed: models = models.OneToOneField(
        Completed, on_delete=models.CASCADE, related_name="completed_todo"
    )
