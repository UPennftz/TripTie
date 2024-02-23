from django.test import TestCase
from django.urls import reverse

class YourAppTests(TestCase):
    def test_search_youtube(self):
        response = self.client.get(reverse('your_view_name'), {'city': 'New York'})
        self.assertEqual(response.status_code, 200)

