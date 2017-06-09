#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import redis

reload(sys)
sys.setdefaultencoding("utf-8")

#连接redis
conn=redis.Redis()   #或者conn=redis.Redis('localhost'),conn=redis.Redis('localhost',6379)效果相同

#redis基本操作
print conn.keys('*')                           #列出所有的键，等同于conn.keys()
conn.set('secret','ni!')                       #给键secret键赋值ni！secret键原来不存在
print conn.keys()                                #列出所有的键
print conn.get('secret')                         #获取指定键的对应值
conn.setnx('secret','icky-icky-icky-ptang-zoop-boing!')   #只有当键不存在时才设定值
print conn.get('secret')                                      #依然返回旧值
print conn.getset('secret','icky-icky-icky-ptang-zoop-boing!')    #返回旧值，同时赋新值
print conn.get('secret')                                       #得到新值
print conn.getrange('secret',-6,-1)                            #得到子字符串，（偏移量offset：0代表开始，-1代表结束）
conn.setrange('secret',5,'ICKY')                               #从开始位置偏移（5）替换字符串
print conn.get('secret')
conn.mset({'pie':'cherry','cordial':'sherry'})               #一次性设置多个键值
print conn.mget('secret','myKey','pie','cordial')            #一次性获取多个键的值






# if __name__ == '__main__':
#     pass