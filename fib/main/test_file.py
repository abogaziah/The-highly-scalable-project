from django.urls import reverse
from django.test import Client

def test_main_view():
    client = Client()
    response = client.get(reverse('index') + '/?x=5', follow=True)
    assert (int(response.content) == 5)
