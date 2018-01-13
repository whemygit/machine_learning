#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import time
import sched
from threading import Timer
import random

reload(sys)
sys.setdefaultencoding("utf-8")

# def worker(msg,starttime):
#     print "执行任务的时刻：",time.time(),"传达的消息是：",msg,"任务建立时刻：",starttime
#
#
# print u'----------  两个简单的例子  -------------'
# print u'程序启动时刻：', time.time()
# s = sched.scheduler(time.time, time.sleep)
# s.enter(1, 1, worker, ('hello', time.time()))
# s.enter(3, 1, worker, ('world', time.time()))
# s.run()  # 这一个 s.run() 启动上面的两个任务
# print u'睡眠２秒前时刻：', time.time()
# time.sleep(2)
# print u'睡眠２秒结束时刻：', time.time()


count = 0
def loopfunc():
    # global count
    s=random.randint(1,100)
    # count += 1
    for i in range(3):
        Timer(3, loopfunc).start()
        return s

# Timer(3, loopfunc, ('world %d' % (count), time.time())).start()


# print random.randint(1, 100)


def randomNum():
    s = random.randint(1, 100)
    return s

def random3Num():
    for i in range(3):
        num =randomNum();
        print num

count = 0
def timerUtil():
    global count
    count += 1
    if count < 3:
        # print count
        Timer(3, random3Num()).start()



def test():
    count = 0

    def loopfunc(msg, starttime):
        global count
        print u'启动时刻：', starttime, ' 当前时刻：', time.time(), '消息 --> %s' % (msg)
        count += 1
        if count < 3:
            Timer(3, loopfunc, ('world %d' % (count), time.time())).start()

    Timer(3, loopfunc, ('world %d' % (count), time.time())).start()


import threading

# def fun_timer():
#     print('Hello Timer!')
#
#
# # if __name__ == '__main__':
# timer = threading.Timer(1, fun_timer)
# timer.start()


def fun_timer():
    # print('Hello Timer!')
    # random3Num()
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()

