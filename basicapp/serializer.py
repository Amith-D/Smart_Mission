from rest_framework import serializers
from basicapp.models import Student

class StudentSerializers(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'
