from django.shortcuts import render
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework import status  # type: ignore
from restApp.models import Student
from restApp.serializers import StudentSerializer
# Create your views here.


# this @api_view decorator is used to tell Django that this function is an API view and only these requests will be handled
# if any request apart from thee below are made, the function will return a 405 error "METHOD NOT ALLOWED"

class StudentList(APIView):
    '''
        APIView by default provides a get method, post method, put method and delete method.
        so whenever a person do a get request, get() will be called.
    '''

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    '''
        here pk is the primary key of the student, which is the id of the student.
        if the pk is not found, it will return a 404 status code
    '''

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
