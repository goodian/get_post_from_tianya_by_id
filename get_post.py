#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#      Filename: get_post.py
#
#        Author: g.goodian@gmail.com
#   Description: ---
#        Create: 2018-09-05 10:40:23
# Last Modified: 2018-09-05 16:41:07
#
import os
import sys
import re
import urllib2

from bs4 import BeautifulSoup

OUTPUT_FILE_NAME = "output"

USER = "kkndme"
ART_ID = 252774
URL = "http://bbs.tianya.cn/m/post-house-{}-{}.shtml"
PAGE_COUNT = 574

fout = open(OUTPUT_FILE_NAME + ".txt", 'w')

def http_request_get(url):
    if not url or len(url) == 0:
        print "http_request_get err: url is None"
    h = urllib2.Request(url)
    return urllib2.urlopen(h)
#end http_request_get

def write_doc(date, text):
    if date is not None: 
        fout.write("\n=================\n")
        fout.write("time: %s\n" % date)

    if text is not None: fout.write("%s\n" % text)
#end write_doc

def write_div_to_doc(date, divs):
    # write date
    write_doc(date, None)

    for d in divs:
        for p in d.find_all():
            write_doc(None, p.text.encode("utf-8"))
            
#end write_div_to_doc

def do_get_copy(url):
    html = http_request_get(url)
    bsObj = BeautifulSoup(html,"html.parser")

    for link in bsObj.find_all("div", attrs={"data-user": USER}):
        if "item-zt" in link["class"]:
            date = link.find("p", class_ = "time fc-gray").text.encode("utf-8")
            write_div_to_doc(date, link.find_all("div", class_ = "bd"))
        else:
            date = link["data-time"]
            write_div_to_doc(date, link.find_all("div", class_ = "reply-div"))

#end do_get_copy

if __name__ == "__main__":
    for i in range(PAGE_COUNT):
        url = URL.format(str(ART_ID), str(i + 1))
        do_get_copy(url)
    #end for
    fout.close()
    print("Done...")

#end if
