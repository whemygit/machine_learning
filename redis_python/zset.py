#!/usr/bin/env python
# -- coding: utf-8 --

#redis有序集合
import sys
import time
import redis

reload(sys)
sys.setdefaultencoding("utf-8")

now = time.time()
conn=redis.Redis()
conn.zadd('logins','smeagol',now)            #增加第一个访客
conn.zadd('logins','bibl',now+(60*3))        #三分钟后增加第二个访客
print conn.zrank('logins','smeagol')        #查看指定访客的登录排名次序
print time.strftime('%c',time.localtime(conn.zscore('logins','bibl')))     #查看指定访客登录时间，为便于观察，将数值型转换为字符串型时间
print conn.zscore('logins','smeagol')
print conn.zrange('logins',0,-1)              #按照登录顺序查看每一位访客
print conn.zrange('logins',0,-1,withscores=True)   #查看登录顺序，并附带登录时间


# if __name__ == '__main__':
#     pass