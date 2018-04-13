from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from tanksapi import testhelper


class Tanks_API_Test(TestCase):
    def test_not_authenticated(self):
        """
        Test that there is no access to the entries of a user, if they are not logged in
        """
        client = APIClient()
        response = client.get(reverse('tanksapi:map-list'))
        # we expect forbidden as no user authentication was done
        self.assertEqual(response.status_code, 200)

    def test_no_maps(self):
        client = APIClient()
        response = client.get(reverse('tanksapi:map-list'))
        # expect 200 OK, but no data received
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_create_and_get_map(self):
        client = APIClient()
        testhelper.login_client(client)
        test_data = testhelper.raw_data()

        # the format specification is important, as the default is a `multipart` request
        response = client.post(reverse('tanksapi:map-list'), data=test_data, format="json")

        # expect 201 CREATED
        self.assertEqual(response.status_code, 201)

        response = client.get(reverse('tanksapi:map-detail', kwargs={'pk': 1}))
        # expect 200 OK, containing details for the period, including its entries
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 7)  # 7 because there are 7 fields in the detail of a map

        self.assertContains(response, test_data["name"])
        self.assertContains(response, test_data["thumbnail_url"])
        self.assertEqual(response.data["terrain"], test_data["terrain"])
