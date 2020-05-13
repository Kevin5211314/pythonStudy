#!/usr/bin/python3
# -*- coding: UTF-8 -*-s

import itchat
import time

itchat.auto_login(hotReload=True) # 热加载

friends = itchat.get_friends(update=True)
lenght = len(friends)
 
for i in range(1, lenght):
    print(f'检测到第{i}位好友: {str(friends[i]["NickName"]).center(20, " ")}')
    print()


itchat.run()


#     # 微信bug，用自己账户给所有好友发送"ॣ ॣ ॣ"消息，当添加自己为好友时，只有自己能收到此信息，如果没添加自己为好友\
#     # 没有人能收到此信息，笔者此刻日期为2019/1/6 8:30，到目前为止微信bug还没修复。
#     # 所以迭代从除去自己后的第二位好友开始 range(1, lenght)。
#     itchat.send("జ్ఞా", toUserName=friends[i]['UserName'])
#     print(f'检测到第{i}位好友: {str(friends[i]["NickName"]).center(20, " ")}')
#     # 发送信息速度过快会被微信检测到异常行为。
#     time.sleep(2)   
 
# print('已检测完毕，请在手机端查看结果。')



# 用户多开
# import itchat

# newInstance = itchat.new_instance()
# newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')

# @newInstance.msg_register(itchat.content.TEXT)
# def reply(msg):
#     return msg.text

# newInstance.run()



# 退出及登陆完成后调用特定方法

# import itchat

# import time

# def lc():
#     print('finish login')
# def ec():
#     print('exit')

# itchat.auto_login(loginCallback=lc, exitCallback=ec)
# time.sleep(3)
# itchat.logout()