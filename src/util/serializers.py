# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from rest_framework import serializers

class GeneralResponse(object):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail
        
class GeneralResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    detail = serializers.CharField(max_length=200)
