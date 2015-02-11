# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''
from rest_framework import serializers
from people.models import People, PeopleInterest


class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = People
        fields = ("username", "email", "phone","status")

class PeopleInterestFocusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PeopleInterest
        fields = ("interest",)


class PeopleInterestFocusListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PeopleInterest
        fields = ("interest","activity")