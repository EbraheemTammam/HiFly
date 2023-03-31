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

class Attachment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='attachments',
    )

    def __str__(self):
        return f'{str(self.person)} | {self.title}'

class Effect(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='effects',
    )

    def __str__(self):
        return f'{str(self.person)} | {self.title}'
