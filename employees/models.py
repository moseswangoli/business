from django.db import models
from businesses.models import Business

class Employee(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50, unique=True)
    kra_pin = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.id_number}"