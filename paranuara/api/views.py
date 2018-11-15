from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import People, Companies
from .serializers import PeopleSerializer, CompaniesEmployeesSerializer, FruitsVegetablesSerializer


class FruitsAndVegetablesViewset(viewsets.ReadOnlyModelViewSet):
    """
    Given a person index (or id, name, guid) returns a list of fruits and vegetables they like.
    """
    queryset = People.objects.all()
    serializer_class = FruitsVegetablesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('_id', 'name', 'guid', 'index')


class CompanyEmployeesViewset(viewsets.ReadOnlyModelViewSet):
    """
    Given a company index (or name) returns all its employees.
    """
    queryset = Companies.objects.all()
    serializer_class = CompaniesEmployeesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('index', 'company')


class PeopleViewset(viewsets.ReadOnlyModelViewSet):
    """
    Given a company id (or name) returns all its employees.
    """
    queryset = People.objects.all()
    serializer_class = FruitsVegetablesSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('company__index',)


# @api_view(['GET'])
# def fruits_and_vegetables(request, person_id=None, person_index=None, person_guid=None):
#     """
#     Given 1 person, provide a list of fruits and vegetables they like.
#     :param person_id:
#     :param person_index:
#     :param person_guid:
#     :return: {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
#     """
#     if request.method == 'GET':
#         if person_index is not None:
#             person = People.objects.get(index=person_index)
#         elif person_id is not None:
#             person = People.objects.get(index=person_id)
#         elif person_guid is not None:
#             person = People.objects.get(index=person_guid)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         serializer = FruitsVegetablesSerializer(person)
#         return Response(serializer.data)
#
#     return Response(status=status.HTTP_400_BAD_REQUEST)
