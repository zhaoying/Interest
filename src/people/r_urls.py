# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from django.conf.urls import patterns, url
from people.views import OwnInfo, UserInterestFocusList


urlpatterns = patterns('people.views',
    #===========================================================================
    # read API
    #===========================================================================
    #个人信息
    url(r'^own/$', OwnInfo.as_view(), name='people-regist'),
    #关注的兴趣列表
    url(r'^interest/$', UserInterestFocusList.as_view(), name="people-interest-list")
)
