# -*- coding:utf-8 -*-
# Create your views here.
from rest_framework.generics import CreateAPIView
from people.models import People

class UserRegister(CreateAPIView):
    model = People
    
    def post(self, request, *args, **kwargs):
        username = request.DATA.get("username", None)
        password = request.DATA.get("password", None)
        return 
    