from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('receptionist', 'Receptionist'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Receptionist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username