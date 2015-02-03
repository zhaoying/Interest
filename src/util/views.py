# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''
from rest_framework.generics import CreateAPIView
from util.const import CONST
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse
from util.serializers import GeneralResponse, GeneralResponseSerializer

class ErrorCode(CONST):
    SUCCESS = 0
    FAILURE = 1
    AUTHENTICATION_FAIL = 4000
    INVALID_INPUT = 4001
    INTERNAL_ERROR = 4002
    EXISTED = 4003
    NOT_EXISTED = 4004
    METHOD_NOT_ALLOWED = 4005

    
    MSG = {
        SUCCESS: 'Success',
        FAILURE: 'General failure',
        AUTHENTICATION_FAIL: 'Authenication failure',
        INVALID_INPUT: 'Invalid input',
        INTERNAL_ERROR: 'Internal Error',
        EXISTED: "Has existed", 
        NOT_EXISTED: "Not existed", 
        METHOD_NOT_ALLOWED: "method not allowed",
    }
    
#     ZH_MSG = {
#         SUCCESS: 'Success',
#         FAILURE: 'General Error',
#         AUTHENTICATION_FAIL: 'Authentication Failed',
#         INVALID_INPUT: 'Parament Error',
#         INTERNAL_ERROR: 'Internal Error',
#         EXISTED: "Already Existed", 
#         NOT_EXISTED: "Not Found", 
#         METHOD_NOT_ALLOWED: "Method Not Allowed"
#     }
    
    
def get_error_detail(error_code):
    try:
        return ErrorCode.MSG[error_code]
    except KeyError:
        return 'Unknown error code(%d)' % error_code

def generalResponseData(code, detail=None):
    if detail is None:
        detail = get_error_detail(code)
    serializer = GeneralResponseSerializer(GeneralResponse(code, detail))
    return serializer.data

def generalJsonResponse(status, code, detail=None):
    return HttpResponse(JSONRenderer().render(generalResponseData(code, detail)), 
                        content_type="application/json", status=status)
    
            
class ISCreateAPIView(CreateAPIView):
    
    def post(self, request, *args, **kwargs):
        super(ISCreateAPIView, self).post(request, *args, **kwargs)
        return 
