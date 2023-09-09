from django.db import models
from services.models import Service

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=50)
    nic_number = models.CharField(max_length=12)
    index_number = models.CharField(max_length=7)
    faculty=models.CharField(max_length=20)
    services = models.ManyToManyField(Service)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)