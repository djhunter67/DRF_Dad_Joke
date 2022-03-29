from django.contrib import admin

from api.models import CurrentJokeModel, NextJokeModel

# Register your models here.

admin.site.register(NextJokeModel)
admin.site.register(CurrentJokeModel)
