# THIS IS MYSQL A TEST SCRIPT.

# Reference: http://www.mikusa.com/python-mysql-docs/introduction.html
# Reference: https://pythonspot.com/mysql-with-python/
# Reference: https://stackoverflow.com/questions/155054/mysql-timestamp-column
# Reference: https://stackoverflow.com/questions/15271907/python-mysql-update-working-but-not-updating-table
# Reference: https://www.a2hosting.com/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line
# Reference: https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.5/en/selecting-rows.html

# Instructions to open mysql server on a Rpi:
#
# Please, run the following commands on your Rpi:
#
# $ sudo mysql -u root -p
# ENTER YOUR ROOT PWD
# > CREATE DATABASE mydb;
# > \q
#
# Once the above commands are run, the mysql server is established and then this python script is executed.


#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mydb")

db.autocommit(True)

cur = db.cursor()

cur.execute("CREATE TABLE eid (Readings INT UNSIGNED NOT NULL AUTO_INCREMENT, Temperature FLOAT, Humidity FLOAT, PRIMARY KEY (Readings))")
cur.execute("ALTER TABLE `eid` ADD `Updated` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP")

tmp = 12.98
hmd = 21.55

for x in range(1, 35):
    tmp += 1
    hmd += 1
    cur.execute("INSERT INTO eid (Temperature, Humidity) VALUES (%s, %s)", (tmp, hmd))

#cur.execute("SELECT * FROM eid")
cur.execute("SELECT * FROM eid WHERE Readings <= '30'")
for row in cur.fetchall() :
    print "Readings:\t\t", row[0], "\n", "Temperature:\t\t", row[1], "C", "\n", "Humidity:\t\t", row[2], "%", "\n", "Updated:\t\t", row[3], "\n\n\n\n"
    
cur.execute("DROP TABLE eid")

