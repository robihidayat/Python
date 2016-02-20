#!/usr/bin/python
#html 
import urllib
import re

urls=["http://news.detik.com/berita/3146084/hasil-kunjungan-jokowi-ke-as-pesan-perdamaian-hingga-janji-bos-google"]

i=0
# x=0

these_regex="(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}"
these_regex1="<!-- E:read image orientation if potrait load this -->(.*?)<!-- POLONG -->"

pattern=re.compile(these_regex)
while(i<len(urls)):
        htmlfile=urllib.urlopen(urls[i])
        htmltext=htmlfile.read()
        titles=re.findall(pattern,htmltext)
        titles1=re.findall(pattern1,htmltext)
        print titles1
        print titles
        i+=1


# pattern1=re.compile(these_regex1)
# while(x<len(urls)):
#         htmlfile=urllib.urlopen(urls[x])
#         htmltext=htmlfile.read()
#         titles1=re.findall(pattern1,htmltext)
#         print titles1
#         x+=1
