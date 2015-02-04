# -*- coding:utf-8 -*-
# Create your views here.
from people.models import People
from util.views import ISCreateAPIView, ISRetrieveAPIView, generalJsonResponse,\
    ErrorCode
from people.serializers import PeopleSerializer
from rest_framework import status
from mongoengine.django.auth import make_password

class UserRegister(ISCreateAPIView):
    u'''用户注册'''
    model = People
    serializer_class = PeopleSerializer
    
    def post(self, request, *args, **kwargs):
        password = self.request.DATA.get("password", None)
        username = self.request.DATA.get("username", None)
        if not username or not password:
            return generalJsonResponse(status.HTTP_200_OK, ErrorCode.INVALID_INPUT)
        return super(UserRegister, self).post(request, *args, **kwargs)
    
    def pre_save(self, serializer_obj):
        password = self.request.DATA.get("password", None)
        serializer_obj.password = make_password(password)
        super(UserRegister, self).pre_save(serializer_obj)
        

class OwnInfo(ISRetrieveAPIView):
    u'''用户获取个人信息'''
    model = People
    serializer_class = PeopleSerializer
    
    def get_object(self):
        return self.request.user