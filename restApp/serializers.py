from rest_framework import serializers  # type: ignore
from restApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'age', 'email')
