from django.contrib.auth.models import AbstractUser
from django.db import models
from services.models import Service


class User(AbstractUser):
    reg_number = models.CharField(max_length=12, unique=True)
    faculty = models.CharField(max_length=30)
    services = models.ManyToManyField(Service)
