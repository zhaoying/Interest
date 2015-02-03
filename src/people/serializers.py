# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''
from rest_framework import serializers
from people.models import People


class PeopleSerializer(serializers):
    
    class Meta:
        model = People