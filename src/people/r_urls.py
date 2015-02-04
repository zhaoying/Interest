# -*- coding:utf-8 -*-
'''
Created on Feb 3, 2015

@author: mzy
'''

from django.conf.urls import patterns, url
from people.views import OwnInfo


urlpatterns = patterns('people.views',
    #===========================================================================
    # read API
    #===========================================================================
    url(r'^own/$', OwnInfo.as_view(), name='people-regist'),
)
