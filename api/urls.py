from django.urls import path

from api.views import CurrentDadJoke, NextDadJoke

app_name = "api"

urlpatterns = [
    path("", CurrentDadJoke.as_view(), name="current_joke"),
    path("next/", NextDadJoke.as_view(), name="next_joke"),
]
