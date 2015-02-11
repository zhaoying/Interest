# -*- coding:utf-8 -*-
from django.db import models
from util.const import CONST

# Create your models here.

class Interest(CONST):
    #BALL = 1
    FOOTBALL = 10
    BASKETBALL = 20
    PINGPANGBALL = 30
    RUNING = 40
    DANCE = 50
    SING = 60
    
    MAP = {
           FOOTBALL : u"football",
           BASKETBALL : "basketball",
           PINGPANGBALL : "ping pang ball",
           RUNING : "runing",
           DANCE : "dance",
           SING : "sing"
           }
    ZH_MAP = {
            u"足球":FOOTBALL,
            u"篮球":BASKETBALL,
            u"乒乓球":PINGPANGBALL,
            u"跑步":RUNING,
            u"跳舞":DANCE,
            u"唱歌":SING
            }