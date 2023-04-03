import os

from django.db import models


class Person(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    religion = models.CharField(max_length=10)
    social_status = models.CharField(max_length=10)
    degree = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField()
    national_id = models.CharField(max_length=14)
    governorate = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    dad_phone_number = models.CharField(max_length=13)
    mom_phone_number = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(Person):
    pass

class Student(Person):
    level = models.IntegerField()
    semester = models.IntegerField()
    year_joined =models.PositiveIntegerField()
    graduated = models.BooleanField(default=False)

def attachment_upload_path(instance, filename):
    return f'attachments/{instance.person.code}/{filename}'

class Attachment(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='attachments',
    )
    file = models.FileField(upload_to=attachment_upload_path)

    def __str__(self):
        return f'{str(self.person)} | {self.title}'

def effect_upload_path(instance, filename):
    return f'effects/{instance.person.code}/{filename}'

class Effect(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='effects',
    )
    file = models.FileField(
        upload_to=effect_upload_path, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f'{str(self.person)} | {self.title}'

def post_delete_signal(sender, instance, *args, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

def attachment_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.pk: return False
    try:
        old = Attachment.objects.get(pk=instance.pk).file
    except Attachment.DoesNotExist:
        return False
    if not old:
        return False
    new = instance.file
    if not new:
        instance.file = old
        return True
    if not old == new:
        if os.path.isfile(old.path):
            os.remove(old.path)

def effect_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.pk: return False
    try:
        old = Effect.objects.get(pk=instance.pk).file
    except Effect.DoesNotExist:
        return False
    if not old:
        return False
    new = instance.file
    if not new:
        instance.file = old
        return True
    if not old == new:
        if os.path.isfile(old.path):
            os.remove(old.path)
        

models.signals.post_delete.connect(post_delete_signal, sender=Attachment)
models.signals.post_delete.connect(post_delete_signal, sender=Effect)
models.signals.pre_save.connect(attachment_pre_save_signal, sender=Attachment)
models.signals.pre_save.connect(effect_pre_save_signal, sender=Effect)
