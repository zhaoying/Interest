# -*- coding:utf-8 -*-
'''
Created on Jan 28, 2015

@author: mzy
'''
from InterestSocial import settings
import mongoengine
from mongoengine.document import Document

#===============================================================================
# 是否需要单例模式
#===============================================================================
mongo_conf = settings.IS_CONFIG['mongo']
mongoengine.connect(**mongo_conf)

def get_mongo_db():
    return mongoengine.connection.get_db()


class ISDocument(Document):
    last_update_time = mongoengine.DateTimeField()
    is_active = mongoengine.BooleanField(defalut=True)