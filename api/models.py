from django.db import models

# Create your models here.


class CurrentJokeModel(models.Model):
    """Store previously gathered jokes"""

    joke: models = models.CharField(max_length=10000, name="present joke")


class NextJokeModel(models.Model):
    """Store the next joke to be presented"""

    joke: models = models.CharField(max_length=10000, name="next joke")

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
