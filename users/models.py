from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    matric_number = models.IntegerField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

