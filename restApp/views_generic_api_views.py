from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  # type: ignore
from restApp.models import Student
from restApp.serializers import StudentSerializer


class StudentList(ListCreateAPIView):
    '''
        ListCreateAPIView: Extends Extends: GenericAPIView, ListModelMixin, CreateModelMixin
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    '''
        RetrieveUpdateDestroyAPIView: Extends Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
