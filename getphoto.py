#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""导入模块"""
import requests  # 导入requests库
import re  # 导入正则表达式库
import os  # 导入操作系统库
import time  # 导入时间库

print('若想停止请按ctrl+C')

if not os.path.exists('iso图片'):  # 判断文件夹是否存在，如果不存在：
    os.mkdir('iso图片')  # 创建一个文件夹
user = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.get('https://isorepublic.com/',headers=user)  # 用requests库的get函数访问总网页，用headers进行伪装，获得所有文章网址
html = response.text  # 用文本显示访问网页得到的内容
urls_wz = re.findall('https://isorepublic.com/wp-content/uploads/.*?.jpg', html)  # 用正则表达式获得文章的所有网址
print(urls_wz)  # 打印显示所有网址
names = re.findall('title="(.*?)" class=', html)  # 正则表达式创建目录名字
print()
print(names)
exit()

#print(names)#显示所有标题
if len(urls_wz):
    for url_wz,name in zip(urls_wz,names):  # 循环获取每一个图片网址
        # 图片的名字
        time.sleep(5)  # 设定5秒延时,太快会GG
        response = requests.get(url_wz, headers=user)  # 用requeste库的get函数访问图片网址，用headers进行伪装
        print("正在保存图片中……")
        print(name)
        with open('./iso图片/'+name+'.jpg', 'wb') as f:  # 用wb模式打开创建文件，w写模式
            f.write(response.content)  # 写入二进制文件内容
    print("保存第1页图片完毕！")
    for i in range(2,100): 
        response = requests.get('https://isorepublic.com/page/'+str(i)+'/',headers=user)
        html = response.text  # 用文本显示访问网页得到的内容
        urls_wz = re.findall('https://isorepublic.com/wp-content/uploads/.*?.jpg', html)
        names = re.findall('title="(.*?)" class=', html)
        if len(urls_wz):
            for url_wz,name in zip(urls_wz,names):  # 循环获取每一个图片网址
                # 图片的名字
                time.sleep(5)  # 设定5秒延时
                response = requests.get(url_wz, headers=user)  # 用requeste库的get函数访问图片网址，用headers进行伪装
                print("正在保存图片中……")
                with open('iso图片/'+name+'.jpg', 'wb') as f:  # 用wb模式打开创建文件，w写模式
                    f.write(response.content)  # 写入二进制文件内容
            print("保存第"+str(i)+"页图片完毕！")
        else:
            print('保存失败')
else:
    print('保存失败')