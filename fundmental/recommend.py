#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
from numpy import *
import random
reload(sys)
sys.setdefaultencoding("utf-8")


#random函数
random.seed(10)    #设定每次生成的随机数是同一个数
random.random()
random.uniform(5,10)
random.randint(5,10)
random.randrange(10, 100, 2)
random.choice(["JGood", "is", "a", "handsome", "boy"])

b=random.randint(5,10)
print b

p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
print p


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 1)
print slice

print random.uniform(5,10)
print random.randint(5,10)
# if __name__ == '__main__':
#     pass