import MySQLdb

import urllib2
import re
import sys

#connect to url 
url=sys.argv[1]
website = urllib2.urlopen(url)

#connect to database
db = MySQLdb.connect("localhost","root","root","url_data" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

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

print linkss
	# Create table as per requirement
# #save to ataframe
#df = pd.DataFrame(linkss, columns=['url_detik'])
#df = df.drop_duplicates()
#print df
sql = "INSERT INTO namaUrl(DATA_URL)\
		VALUES ('%s')" %\
		("")

try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
# # create and save to sqlite database
# detik_db = create_engine('sqlite:///detiks.db')
# df.to_sql('url_detik', detik_db)

# #save to csv file
# df.to_csv('datalinks.csv',index=False,header=False)
# Location = r'/home/robihidayat/Workshop/Python/datalinks.csv'
# df = pd.read_csv(Location)
#for link in links: