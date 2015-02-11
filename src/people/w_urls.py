# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from django.conf.urls import patterns, url
from people.views import UserRegister, UserInterestFocus


urlpatterns = patterns('people.views',
    #===========================================================================
    # write API
    #===========================================================================
    # 用户注册
    url(r'^$', UserRegister.as_view(), name='people-regist'),
    # 用户选择兴趣, 关注某个兴趣
    url(r'^interest/$', UserInterestFocus.as_view(), name="user-interest-focus")

)
