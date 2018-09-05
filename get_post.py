#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#      Filename: get_post.py
#
#        Author: g.goodian@gmail.com
#   Description: ---
#        Create: 2018-09-05 10:40:23
# Last Modified: 2018-09-05 14:35:48
#
import os
import sys
import re
import urllib2
from bs4 import BeautifulSoup

OUTPUT_FILE = "output.txt"

USER = "kkndme"
ART_ID = 252774
URL = "http://bbs.tianya.cn/m/post-house-{}-{}.shtml"
PAGE_COUNT = 574

fout = open(OUTPUT_FILE, 'w')

def http_request_get(url):
    if not url or len(url) == 0:
        print "http_request_get err: url is None"
    h = urllib2.Request(url)
    return urllib2.urlopen(h)
    #ht = urllib2.urlopen(h)
    #html = ht.read()
    #return html
#end http_request_get

def write_doc(date, text):
    fout.write("\n=================\n")
    fout.write("date-time:" + date)
    fout.write(text)
#end write_doc

def do_get_copy(url):
    html = http_request_get(url)
    bsObj = BeautifulSoup(html,"html.parser")
    for link in bsObj.find_all("div", class_ = "item item-zt item-lz"):
        print link
        date = link.find("p", class_ = "time fc-gray").text
        text = link.find("div", class_="bd").text.encode("utf-8")
        write_doc(date, text)

    for link in bsObj.find_all("div", class_ = "item item-ht item-lz"):
        date = link["data-time"]
        text = link.find("div", class_="reply-div").text.encode("utf-8")
        write_doc(date, text)

#end do_get_copy

if __name__ == "__main__":
    print("aa")
    for i in range(PAGE_COUNT):
        url = URL.format(str(ART_ID), str(i + 1))
        do_get_copy(url)
    #end for
    fout.close()
#end if
