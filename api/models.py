from django.db import models

# Create your models here.

<<<<<<< HEAD

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
=======
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


# Store previously gathered jokes

# Store searched terms

>>>>>>> trunk
