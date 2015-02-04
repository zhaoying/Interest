from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class People(AbstractUser):
    phone = models.CharField(max_length=64, blank=True, unique=True, null=True, db_index=True)
    address = models.CharField(max_length=128, blank=True, null=True)