from restApp.serializers import StudentSerializer
from restApp.models import Student
from rest_framework import status  # type: ignore
from typing import Generic
from django.shortcuts import render
from rest_framework.response import Response  # type: ignore
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin  # type: ignore
from rest_framework.generics import GenericAPIView  # type: ignore
# Create your views here.


# this @api_view decorator is used to tell Django that this function is an API view and only these requests will be handled
# if any request apart from thee below are made, the function will return a 405 error "METHOD NOT ALLOWED"

class StudentList(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''
        queryset is the default set, on which mixins wilol perform the action
        serializer_class is the default serializer class, on which mixins will perform the action

        .list() is provided by ListModelMixin, which is a generic view for getting a list of objects from provided queryset and serializer class
        .create() is provided by CreateModelMixin, which is a generic view for creating a new object from provided serializer class
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    '''
        queryset is the default set, on which mixins wilol perform the action
        serializer_class is the default serializer class, on which mixins will perform the action

        .retrieve() is provided by RetrieveModelMixin, which is a generic view for getting a single object from provided queryset and serializer class
        .update() is provided by UpdateModelMixin, which is a generic view for updating a single object from provided serializer class
        .destroy() is provided by DestroyModelMixin, which is a generic view for deleting a single object from provided serializer class
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
