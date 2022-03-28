from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.models import Todo

# Create your views here.

class TodoView(APIView):
    """Return infmation regarding the todo object"""

    def get(self) -> Response:

        todo_item = get_object_or_404(Todo.objects.select_related("completed_todo"))

        print([todo for todo in range(todo_item.count())])

        return Response([todo for todo in range(todo_item.count())], status=status.HTTP_200_OK)

    def post(self, request):

        input_data = request.data

        print(input_data)

        return Response(status=status.HTTP_200_OK)

    

