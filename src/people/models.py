from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.



class People(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=64, unique=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    email = models.EmailField(blank=True, null=True, nnique=True, db_index=True)
    phone = models.CharField(max_length=64, blank=True, null=True, db_index=True)
    address = models.CharField(max_length=128, blank=True, null=True)