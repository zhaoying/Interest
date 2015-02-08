# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class People(AbstractUser):
    phone = models.CharField(max_length=64, blank=True, unique=True, null=True, db_index=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    #interest = models.ManyToManyField()
    
class PeopleInterest(models.Model):
    people = models.PositiveIntegerField(db_index=True)
    interest = models.PositiveIntegerField(db_index=True)
    #活跃度
    activity = models.PositiveIntegerField(db_index=True)
    