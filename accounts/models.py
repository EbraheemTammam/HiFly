from django.apps import apps
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        username = email.split('@')[0]

        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'admin']

    def __str__(self):
        return self.get_full_name()

def custom_user_pre_save(sender, instance, *args, **kwargs):
    if not instance.username:
        instance.username = instance.email.split('@')[0]
    if instance.is_staff:
        instance.admin = True
    else:
        instance.password = make_password(instance.password)

models.signals.pre_save.connect(custom_user_pre_save, sender=CustomUser)