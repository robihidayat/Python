import MySQLdb as db

import urllib2
import re
import sys


con = db.connect("localhost","root","root","data_detik")
cur = con.cursor()
#cur.execute('CREATE DATABASE data_detik;')
#cur.commit()
#cur.close()

url = sys.argv[1]
link_exr = re.compile(r'<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>')
links = []

# open web content
f = urllib2.urlopen(url)
content = f.read()

for link in link_exr.findall(content):
		if "detik.com" in link[0]:
			link_detik = link[0]
			if "http:" not in link_detik:
				link_detik = "http:" + link_detik
			links.append(link_detik)
			#print(links)

cur.execute('CREATE TABLE data_detiks(data_links VARCHAR(16))')
query = "INSERT INTO linksnya(urlnya)"\
		"VALUES(%s)"
cur.executemany(query,links)
con.commit()

# #buat database table 
# cur.execute('CREATE TABLE data_detik(data_links VARCHAR(16))')
# cur.execute("INSERT INTO linksnya VALUES %s",(links))
# cur.execute("SELECT * FROM linksnya WHERE data_links LIKE '%j'")
# for data in cur.fetchall():
# 	print '%s' %data
# cur.close
# cur.commit()

# # cur.execute('CREATE TABLE data(login VARCHAR(8), uid INT)')
# cur.execute("INSERT INTO users VALUES('john', 7000)")
# cur.execute("INSERT INTO users VALUES('jane', 7001)")
# cur.execute("INSERT INTO users VALUES('bob', 7200)")
# cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")
# for data in cur.fetchall():
#     print '%s\t%s' % data
# cur.execute("UPDATE users SET uid=7100 WHERE uid=7001")
# cur.execute("SELECT * FROM users")
# for data in cur.fetchall():
#     print '%s\t%s' % data
# cur.execute('DELETE FROM users WHERE login="bob"')
# cur.execute('DROP TABLE users')
# cur.close()
# cxn.commit()
# cxn.close()


# for s in range(0,len(alltitles)):
#     print alltitles[s]
#     query = "INSERT INTO table (colname) VALUES ("+alltitles[s]+")"
#     x=conn.cursor()
#     x.execute(query, alltitles[s])
#     row = x.fetchall()



# x = conn.cursor()
# for title in alltitles:
#     print title
#     query = "INSERT INTO table (colname) VALUES (%s)"
#     x.execute(query, title)
#     row = x.fetchall()

