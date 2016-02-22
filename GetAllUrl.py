
from pandas import DataFrame
from sqlalchemy import create_engine

import pandas as pd #this is how I usually import pandas
import urllib2
import re
import sys

#connect to url 
url=sys.argv[1]
website = urllib2.urlopen(url)

linkss=[]
# #read html code
html = website.read()

# #use re findall to get all the links
#parameter (//.*detik?) <a.*?\s*href=\"(.*?)\".*?>(.*?)</a>
links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>",html)

for link in links:
	if "detik.com" in link[0]:
		link_detik = link[0]
		if "http:" not in link_detik:
			link_detik = "http:" + link_detik
		linkss.append(link_detik)
	
# #save to ataframe
df = pd.DataFrame(linkss, columns=['url_detik'])
#df = df.drop_duplicates()
print df

# # create and save to sqlite database
detik_db = create_engine('sqlite:///detiks.db')
df.to_sql('url_detik', detik_db)

# #save to csv file
# df.to_csv('datalinks.csv',index=False,header=False)
# Location = r'/home/robihidayat/Workshop/Python/datalinks.csv'
# df = pd.read_csv(Location)
#for link in links: