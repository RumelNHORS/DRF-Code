from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from . pagination import LimitOffsetPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination