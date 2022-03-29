from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.models import CurrentJokeModel, NextJokeModel
from resources.helpers.dad_joke import Dad_Joke

# Create your views here.


class CurrentDadJoke(APIView):
    """Return the second newest joke in the db"""

    def get(self, request) -> Response:

        joker = Dad_Joke()

        joke_object = CurrentJokeModel(present_joke=joker.get_joke()["joke"])
        joke_object.save()
        next_joke = NextJokeModel(next_joke=joker.get_joke()["joke"])
        next_joke.save()

        return Response(str(joke_object), status=status.HTTP_200_OK)


class NextDadJoke(APIView):
    """Return the lastest joke in the db"""

    def get(self, request) -> Response:

        next_joke_object = get_object_or_404(NextJokeModel)

        return Response(str(next_joke_object))
