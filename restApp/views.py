from django.shortcuts import render
from rest_framework.response import Response  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from rest_framework import status  # type: ignore
from restApp.models import Student
from restApp.serializers import StudentSerializer
# Create your views here.


# this @api_view decorator is used to tell Django that this function is an API view and only these requests will be handled
# if any request apart from thee below are made, the function will return a 405 error "METHOD NOT ALLOWED"
@api_view(['GET', 'POST'])
def student_list(request):
    '''
        is_valid() method is used to validate the data.

        DRF has own status codes for success and failure, so we can use them instead of the status code
        status.HTTP_200_OK = 200
        status.HTTP_201_CREATED = 201
        status.HTTP_202_ACCEPTED = 202
        status.HTTP_400_BAD_REQUEST = 400
        status.HTTP_404_NOT_FOUND = 404
        status.HTTP_500_INTERNAL_SERVER_ERROR = 500

        serializer.errors is a dictionary, which handles errors gracefully, 

        like if I do add a invalid email, it will return a dictionary with the key 'email' and the value 'Enter a valid email address.'

        "email": [
            "Enter a valid email address."
        ]

    '''

    if request.method == 'GET':
        students = Student.objects.all()
        # many because we are returning a list of students
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    '''
        here pk is the primary key of the student, which is the id of the student.
        if the pk is not found, it will return a 404 status code
    '''
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
