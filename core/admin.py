from django.contrib import admin

from .models import Student, Employee, Attachment, Effect


admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Attachment)
admin.site.register(Effect)