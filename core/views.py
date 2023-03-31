from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
)

from .serializers import (
    StudentSerializer, 
    EmployeeSerializer,
    AttachmentSerializer,
    EffectSerializer
)
from .models import Student, Employee, Attachment, Effect

class StudentListApiView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EmployeeListApiView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttachmentListApiView(ListCreateAPIView):
    serializer_class = AttachmentSerializer

    def get_queryset(self, *args, **kwargs):
        student = self.request.query_params.get('student')
        if student:
            return Attachment.objects.filter(person__pk=student)
        employee = self.request.query_params.get('employee')
        if employee:
            return Attachment.objects.filter(person__pk=employee)
        return Attachment.objects.all()

class AttachmentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

class EffectListApiView(ListCreateAPIView):
    serializer_class = EffectSerializer

    def get_queryset(self, *args, **kwargs):
        student = self.request.query_params.get('student')
        if student:
            return Effect.objects.filter(person__pk=student)
        employee = self.request.query_params.get('employee')
        if employee:
            return Effect.objects.filter(person__pk=employee)
        return Effect.objects.all()

class EffectDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer