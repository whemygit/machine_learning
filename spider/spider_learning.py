#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import requests
from lxml import etree
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

def get_content(url):
    resp=requests.get(url)
    return resp.content

def get_element(content):
    doc=etree.HTML(content)
    ele_res=doc.xpath('//li[@class="cate_menu_item"]')
    # ele_res=doc.xpath('//li[@class="cate_menu_item"]/a/text()')
    return ele_res

def bs_get_element(content):
    doc=BeautifulSoup(content,'lxml')
    ele_res=doc.find_all('a',{'class':'cate_menu_lk'})
    return ele_res


if __name__ == '__main__':
    content=get_content('https://www.jd.com')
    for item in bs_get_element(content):
        print item.get_text()


    # for item in get_element(content):
    #     print item.xpath('a/text()')









