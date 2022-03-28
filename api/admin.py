from django.contrib import admin

from api.models import Completed, Todo

# Register your models here.

admin.site.register(Completed)
admin.site.register(Todo)
