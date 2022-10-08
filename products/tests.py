# testing products app
from django.test import SimpleTestCase


class ProductpageTests(SimpleTestCase):
    """
    Checking that home page returns an http response status of 200
    """

    def test_url_exists_at_correct_location(self):
        """ Testing collections page """
        response = self.client.get('collection')
        self.assertEqual(response.status_code, 200)


class AddproductpageTests(SimpleTestCase):
    """
    Checking that home page returns an http response status of 200
    """

    def test_url_exists_at_correct_location(self):
        """ Testing collections page """
        response = self.client.get('add_product')
        self.assertEqual(response.status_code, 200)


class EditproductpageTests(SimpleTestCase):
    """
    Checking that home page returns an http response status of 200
    """

    def test_url_exists_at_correct_location(self):
        """ Testing collections page """
        response = self.client.get('edit_product')
        self.assertEqual(response.status_code, 200)


class DetailproductpageTests(SimpleTestCase):
    """
    Checking that home page returns an http response status of 200
    """

    def test_url_exists_at_correct_location(self):
        """ Testing collections page """
        response = self.client.get('product_detail')
        self.assertEqual(response.status_code, 200)
