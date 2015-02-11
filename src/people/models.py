# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class People(AbstractUser):
    phone = models.CharField(max_length=64, blank=True, unique=True, null=True, db_index=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    #people status
    STATUS_INIT = 0
    STATUS_REAL_CERT = 10
    STATUS_CHOICES = (
                      (STATUS_INIT, "init create"),
                      (STATUS_REAL_CERT, "REAL CERTIFICATION")
                      )
    status = models.PositiveIntegerField(default=STATUS_INIT, choices=STATUS_CHOICES,db_index=True)
    #interest = models.ManyToManyField()
    

class PeopleInterest(models.Model):
    u'''人员和兴趣的对应关系'''
    people = models.PositiveIntegerField(db_index=True)
    interest = models.PositiveIntegerField(db_index=True)
    #活跃度
    activity = models.PositiveIntegerField(default=0, db_index=True)
    #
    is_active = models.BooleanField(default=True, db_index=True)
    
    