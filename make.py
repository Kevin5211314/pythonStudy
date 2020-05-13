#!/usr/bin/python3
# -*- coding: UTF-8 -*-    

"""导入模块"""
import requests  # 导入requests库
import re        # 导入正则表达式库
import os        # 导入操作系统库
import time      # 导入时间库
import sys       # 系统类库
import pymysql   # mysql数据库类库


def getHtmlText(geturl=''):
    print(geturl)
    user = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(geturl ,headers=user)  # 用requests库的get函数访问总网页，用headers进行伪装，获得所有文章网址
    html = response.text
    urls_wz = re.findall('http://img.*.0"', html)  # 用正则表达式获得文章的所有网址
    print(urls_wz)  # 打印显示所有产品图片
    # for item in urls_wz :
    #     print(item)
    exit()

# 打开数据库连接
db = pymysql.connect("127.0.0.1","root","","luicicms" ,charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM ad_category limit 10"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        if re.match(r'(.*)/spc.*', row[6], re.M|re.I) :
            getHtmlText(row[6])
            
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
