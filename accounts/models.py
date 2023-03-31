from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'admin']

    def __str__(self):
        return self.get_full_name()

def custom_user_pre_save(sender, instance, *args, **kwargs):
    if not instance.username:
        instance.username = instance.email.split('@')[0]

models.signals.pre_save.connect(custom_user_pre_save, sender=CustomUser)