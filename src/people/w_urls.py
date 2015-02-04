# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from django.conf.urls import patterns, url
from people.views import UserRegister


urlpatterns = patterns('people.views',
    #===========================================================================
    # write API
    #===========================================================================
    # 用户注册
    url(r'^$', UserRegister.as_view(), name='people-regist'),
    #===========================================================================
    # read API
    #===========================================================================

)
