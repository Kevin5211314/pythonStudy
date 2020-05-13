#!/usr/bin/python3
# -*- coding: UTF-8 -*-s

"""导入模块"""
import urllib.request

rqs = urllib.request.urlopen('http://www.baidu.com')

html = rqs.read()
