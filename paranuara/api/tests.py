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

    def tearDown(self):
        """Destroy resources and remove temporaries after test."""

    def test_model_can_create_people(self):
        """Test the People model can create a person."""
        person = People(index=0)
        old_count = People.objects.count()
        person.save()
        new_count = People.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_companies(self):
        """Test the Companies model can create a company."""
        company = Companies(index=0)
        old_count = Companies.objects.count()
        company.save()
        new_count = Companies.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.person1 = {
            'name': 'John Doe',
            'index': 1,
        }
        self.person2 = {
            'name': 'Jane Doe',
            'index': 2,
        }
        company = Companies(index=1)
        company.save()
        People(company=company, **self.person1).save()
        People(company=company, **self.person2).save()
        self.client = APIClient()

    def test_api_twopeople(self):
        """Test the api can get two people."""
        response = self.client.get(reverse('twopeople', kwargs={'pk1': self.person1['index'], 'pk2': self.person2['index']}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1['name'])
        self.assertContains(response, self.person2['name'])

    def test_api_can_get_employees(self):
        """Test the api can get employees."""
        response = self.client.get(reverse('employees-detail', kwargs={'pk': self.person1['index']}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1['name'])
        self.assertContains(response, self.person2['name'])

    def test_api_can_get_fruits_and_vegetables(self):
        """Test the api can get employees."""
        response = self.client.get(reverse('fruits_and_vegetables-detail', kwargs={'pk': self.person1['index']}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.person1['name'])
