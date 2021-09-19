from rest_framework.viewsets import ModelViewSet  # type: ignore
from restApp.models import Student
from restApp.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    ReadOnlyModelViewSet: read only viewset
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
