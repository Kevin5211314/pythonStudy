#!/usr/bin/python3
# -*- coding: UTF-8 -*-    

# 第1种方法
import platform

print(platform.python_version())

variable = list(range(5))

for item in variable:
    print(item, variable[item])


# for x in list(range(5)):
#     print(x)

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()


# # 定义一个方法来计算圆的面积
# def findArea(r):
#     PI = 3.142
#     return PI * (r*r)
 
# # 调用方法
# print("圆的面积为 %.6f" % findArea(5))


# #先设置一个基本的窗口，告诉她要填报一个信息，就以体温填报为例吧
# msg = g.msgbox(msg="为确保工作室能够安全，请您认真填报体温",title="XXXX工作室体温填报系统",ok_button="ok")

# msg = "请填写以下信息(其中带*号的项为必填项)"#填报提示信息
# title = "XXXX工作室体温填报系统"#标题
# fieldNames = ["*姓名","*手机号码","*日期(格式：20200229)","*体温","Email"]#内容和格式
# fieldValues = []#拿个空列表装信息
# fieldValues = g.multenterbox(msg,title,fieldNames)#把信息装进去


# print('开始停止5秒')
# time.sleep(5)#留5秒钟让她记下来
# print('停止5秒结束')