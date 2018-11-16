from django.test import TestCase
from .models import People, Companies
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# from . import views


class ModelTestCase(TestCase):
    """This class defines the test suite for models."""

    def setUp(self):
        """Define the test client and other test variables."""

    def test_model_can_create_people(self):
        """Test the People model can create a person."""
        person = People()
        old_count = People.objects.count()
        person.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_companies(self):
        """Test the Companies model can create a company."""
        company = Companies()
        old_count = Companies.objects.count()
        company.save()
        new_count = Companies.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_api_twopeople(self):
        """Test the api can get a given bucketlist."""
        # employees = Bucketlist.objects.get()
        response = self.client.get(reverse('twopeople', kwargs={'pk1':0, 'pk2':1}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertContains(response, bucketlist)

    def test_api_can_get_employees(self):
        """Test the api can get a given bucketlist."""
        # employees = Bucketlist.objects.get()
        response = self.client.get('/api/employees/2/', format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertContains(response, bucketlist)

