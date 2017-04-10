#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

from urllib import *
from bs4 import BeautifulSoup
# html=urlopen("http://www.pythonscraping.com/pages/page1.html")
# print html.read()
# #
# bsObj=BeautifulSoup(html.read(),'lxml')
# print bsObj
# print bsObj.div

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html.read(),'lxml')
        title=bsObj.h1
    except AttributeError as e:
        return None
    return title

title=getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
    print 'title could not be found'
else:
    print title







