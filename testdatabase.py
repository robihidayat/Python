#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","url_data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Select qSQL with id=4.
cursor.execute("SELECT namaUrl FROM TBLTEST WHERE id = 4")

# Fetch a single row using fetchone() method.
results = cursor.fetchone()

namaUrl = results[0]

cursor.execute(namaUrl)

# Fetch all the rows in a list of lists.
qSQLresults = cursor.fetchall()
for row in qSQLresults:
    id = row[0]
    city = row[1]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    cursor.execute('''INSERT into FACTRESTTBL (id, city)
                  values (%s, %s)''',
                  (id, city))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()