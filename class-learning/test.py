#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class person():
    def __init__(self,name):
        self.name=name

class car():
    def exclaim(self):
        print 'I am a car!'

class yugo(car):
    def exclaim(self):
        print 'I am a yugo!'


if __name__ == '__main__':
    someone=person('hunter')
    print someone.name

    give_me_a_car=car()
    give_me_a_car.exclaim()

    give_me_a_yugo=yugo()
    give_me_a_yugo.exclaim()
