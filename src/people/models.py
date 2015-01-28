# -*- coding:utf-8 -*-
import mongoengine
from util.db import ISDocument


# Create your models here.

'''

MongoEngine字段类型                    Django ORM 对等物
StringField              CharField
URLField                 URLField
EmailField               EmailField
IntField                 IntegerField
FloatField               FloatField
DecimalField             DecimalField
BooleanField             BooleanField
DateTimeField            DateTimeField
EmbeddedDocumentField    None
DictField                None
ListField                None
SortedListField          None
BinaryField              None
ObjectIdField            None
FileField                FileField
'''

class Poople(ISDocument):
    # 账户名
    account_name = mongoengine.StringField(max_length=128,regex=None)
    # 密码
    password = mongoengine.StringField(max_length=128)
    # 邮箱
    email = mongoengine.EmailField()
    # 电话
    phone = mongoengine.StringField(max_length=256)
    # 地址
    address = mongoengine.StringField(max_length=256)
    