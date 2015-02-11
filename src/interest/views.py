# -*- coding:utf-8 -*-
# Create your views here.
from util.views import generalJsonResponse, ErrorCode
from rest_framework import status
from interest.models import Interest
from rest_framework.views import APIView


class InterestListView(APIView):
    
    allow_anonymous = True
    def get(self, request, *args, **kwargs):
        return generalJsonResponse(status.HTTP_200_OK, ErrorCode.SUCCESS, Interest.ZH_MAP)