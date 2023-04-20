from rest_framework.serializers import ModelSerializer, IntegerField, FileField

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
    file = FileField(required=False)
    class Meta:
        model = Attachment
        fields = '__all__'

class EffectSerializer(ModelSerializer):
    file = FileField(required=False)
    class Meta:
        model = Effect
        fields = '__all__'