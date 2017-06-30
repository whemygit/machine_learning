#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import redis

reload(sys)
sys.setdefaultencoding("utf-8")

conn=redis.Redis()

def url_add(url):
    if conn.exists(url):
        pass
        print 'nothing'
    else:
        conn.set(url,1)



if __name__ == '__main__':
    # url_add('a')
    # print conn.keys()
    # conn.expire('a',30)
    print conn.keys()
