#!/usr/bin/python

'''
'''

from sqlalchemy import create_engine
from pandas import DataFrame
import urllib2
import sys
import re

# from bs4 import BeautifulSoup

def get_link(url):
	link_exr = re.compile(r'<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>')
	links = []
	
	# open web content
	f = urllib2.urlopen(url)
	content = f.read()
	
	# versi find html tag : find all url and save to links
	# soup = BeautifulSoup(content, "lxml")
	# for a in soup.find_all('a', href=True):
	# 	if "detik.com" in a['href']:
	# 		if "http:" not in a['href']:
	# 			a['href'] = "http:" + a['href']
	# 		print "Found the URL:", a['href']
	# 		links.append(a['href'])
			
	# versi regex : find all url and save to links			
	for link in link_exr.findall(content):
		if "detik.com" in link[0]:
			link_detik = link[0]
			if "http:" not in link_detik:
				link_detik = "http:" + link_detik
			links.append(link_detik)
	
	# save to DataFrame
	df = DataFrame(links, columns=['detik url'])
	df.drop_duplicates()

	print df.head(0)
		# create and save to sqlite database
	detik_db = create_engine("mysql://root:root@localhost/data_detik") 
	df.to_sql('url_detik', detik_db, if_exists='replace')
		
if __name__ == "__main__":
	url = sys.argv[1]
	get_link(url)