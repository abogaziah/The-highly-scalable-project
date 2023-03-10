from django.test import TestCase
from django.urls import reverse


class YourTestClass(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('index')+'/?x=5', follow=True)
        assert(int(response.content)==5)