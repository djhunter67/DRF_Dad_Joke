from django.test import SimpleTestCase
from django.urls import resolve, reverse

from api.views import CurrentDadJoke, NextDadJoke


class TestURLs(SimpleTestCase):
    def test_current_joke_url_resolves(self):
        url = reverse("api:current_joke")
        assert resolve(url).func.view_class, CurrentDadJoke

    def test_next_joke_url_resolves(self):
        url = reverse("api:next_joke")
        assert resolve(url).func.view_class, NextDadJoke
