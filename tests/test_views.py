from unittest import skip

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


class ViewsTestCase(APITestCase):

    databases = "__all__"

    def setUp(self) -> None:
        self.current_joke = reverse("api:current_joke")
        self.next_joke = reverse("api:next_joke")

    def test_current_joke_get_status_code(self):

        response = self.client.get(self.current_joke)
        assert response.status_code, status.HTTP_200_OK

    def test_next_joke_get_status_code(self):

        response = self.client.get(self.next_joke)
        assert response.status_code, status.HTTP_200_OK
