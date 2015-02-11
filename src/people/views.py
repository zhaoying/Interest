# -*- coding:utf-8 -*-
# Create your views here.
from people.models import People, PeopleInterest
from util.views import ISCreateAPIView, ISRetrieveAPIView, generalJsonResponse,\
    ErrorCode, ISListAPIView
from people.serializers import PeopleSerializer, PeopleInterestFocusSerializer,\
    PeopleInterestFocusListSerializer
from rest_framework import status
from mongoengine.django.auth import make_password

class UserRegister(ISCreateAPIView):
    u'''用户注册'''
    
    model = People
    serializer_class = PeopleSerializer
    allow_anonymous = True
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


class UserInterestFocus(ISCreateAPIView):
    u'''用户选择感兴趣的兴趣, 关注某个兴趣'''
    
    model = PeopleInterest
    serializer_class = PeopleInterestFocusSerializer
    
    def pre_save(self, obj):
        obj.people = self.request.user.id
        super(UserInterestFocus, self).pre_save(obj)
        

class UserInterestFocusList(ISListAPIView):
    model = PeopleInterest
    serializer_class = PeopleInterestFocusListSerializer
    
    def get_queryset(self):
        qs = super(UserInterestFocusList, self).get_queryset()
        qs.filter(people=self.request.user.id)
        return qs
    
    
    