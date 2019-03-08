# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0008 19:56
# @Author  : __Yanfeng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from student import views as st_views

urlpatterns = [
    url(r'index$', st_views.index, name='index')
]
