from django.shortcuts import render
from . serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from . models import Student
#filter for per view
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    #queryset = Student.objects.filter(passby='admin')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['city']
    filterset_fields = ['city', 'name']
