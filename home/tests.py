# pylint: disable=missing-function-docstring
from django.test import SimpleTestCase

# Create your tests here.


class IndexpageTests(SimpleTestCase):
    """
    Checking that home page returns an http response status of 200
    """
    def test_url_exists_at_correct_location(self):
        response = self.client.get('home')
        self.assertEqual(response.status_code, 200)


class ContactFormTests(SimpleTestCase):
    """
    Checking that when you sumbit the form in index page return http
    response status of 200
    """
    def test_url_exists_at_correct_location(self):
        response = self.client.get('contactForm_submit')
        self.assertEqual(response.status_code, 200)
