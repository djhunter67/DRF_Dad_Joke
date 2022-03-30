from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CurrentJokeModel(models.Model):
    """Store previously gathered jokes"""

    joke = models.CharField(max_length=10000, name="present_joke")
    # created = models.OneToOneField(TimeStampedModel,  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.present_joke}"


class NextJokeModel(models.Model):
    """Store the next joke to be presented"""

    joke = models.CharField(max_length=10000, name="next_joke")

    def __str__(self) -> str:
        return f"{self.next_joke}"
