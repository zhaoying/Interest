# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from django.conf.urls import patterns, url
from people.views import OwnInfo
from interest.views import InterestListView


urlpatterns = patterns('people.views',
    #===========================================================================
    # read API
    #===========================================================================
    #兴趣列表
    url(r'^$',InterestListView.as_view(), name="interest-list")
)
