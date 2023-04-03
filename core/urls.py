from django.urls import path

from .views import (
    #   student views
    StudentListApiView,
    StudentDetailApiView,
    #   employee views
    EmployeeListApiView,
    EmployeeDetailApiView,
    #   attachment views
    AttachmentListApiView,
    AttachmentDetailApiView,
    #   effect views
    EffectListApiView,
    EffectDetailApiView,
)

app_name = 'core'


urlpatterns = [
    #   student endpoints
    path('students/', StudentListApiView.as_view()),
    path('students/<int:pk>/', StudentDetailApiView.as_view()),
    #   employee endpoints
    path('emolyees/', EmployeeListApiView.as_view()),
    path('employees/<int:pk>/', EmployeeDetailApiView.as_view()),
    #   attachment endpoints
    path('attachments/', AttachmentListApiView.as_view()),
    path('attachments/<int:pk>/', AttachmentDetailApiView.as_view()),
    #   effect endpoints
    path('effects/', EffectListApiView.as_view()),
    path('effects/<int:pk>/', EffectDetailApiView.as_view()),
]