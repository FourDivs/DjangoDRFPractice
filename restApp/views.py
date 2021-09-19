from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def student_list(request):
    student = {
        'name': 'Dhruv',
        'marks': 50
    }
    return Response(student)
