#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 22:07
# @Author  : Lone
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from Two import views

urlpatterns = [
   path('index/', views.index)
]