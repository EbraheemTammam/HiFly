from rest_framework.serializers import ModelSerializer, IntegerField

from .models import Student, Employee, Attachment, Effect


class StudentSerializer(ModelSerializer):
    code = IntegerField(required=False)
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    code = IntegerField(required=False)
    class Meta:
        model = Employee
        fields = '__all__'

class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class EffectSerializer(ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'