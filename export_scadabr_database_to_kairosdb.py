#!/bin/python3
import requests
import gzip
import json
import sys
import mysql.connector as mariadb

cursor = None

# Connects to the MySQL/MariaDB database.
# 
# db: the name of MySQL/MariaDB schema to be exported. 
#     Default schema name for ScadaBR is 'scadabr'.
#
# user: the username for the database. 
#		Default is root.
#
# passwd: the password for the given username.
# 		Default is empty. 
#
def connect(db='scadabr', user='root', passwd=''):
	mariadb_connection = mariadb.connect(user=user, \
									 password=passwd, \
									 database=db)
	cursor = mariadb_connection.cursor()

# Execute a SQL query on the MySQL/MariaDB database.
#
def execute_query(query):
	try:
		cursor.execute(query)
		return cursor
	except mariadb.Error as error:
		print("Error: {}".format(error))

# Get all information needed from user. It includes:
#
# - Database to be exported.
# - Credentials to access the database (Login/Password for MySQL/MariaDB)
#
def get_info():
	db_name = input("What's the database name you want to export from ScadaBr to KairosDB? Default is 'scadabr'.\nA: ")
	print("\n\nPlease, provide your credentials to the MySQL/MariaDB database.")
	db_user = input("MySQL username:  ")
	db_passwd = input("Password for " + str(db_user) + ":  ")
	return db_name, db_user, db_passwd

# Asking for credentials and database name. After that, connecting to mariadb.
connect(get_info())

# Querying all data (format: <sensor name>, <dataType>, <measured value>, <timestamp in UNIX format> )
query = execute_query("SELECT dataPoints.xid, pointValues.dataType, pointValues.pointValue, pointValues.ts from pointValues \
					  INNER JOIN dataPoints on pointValues.dataPointId=dataPoints.id")

send_to_kairos = []
for row in query:
	temp = {}
	temp["name"] = row[0]
	temp["tags"] = {
		"sensor_name": row[0]
	}
	temp["timestamp"] = row[3]
	temp["value"] = row[2]
	send_to_kairos.append(temp)

# print(send_to_kairos)
print("Length: \n" + str(len(send_to_kairos)))
print("Sending to KairosDB...Depending on how many data you have sent, this may take some minutes.")
print("\n\tFor comparing purposes, we've wait about 15 minutes for \n\t1.7 million point values in a low-end notebook.")

# Gzipping json before send.
gzipped = gzip.compress(bytes(json.dumps(send_to_kairos), 'UTF-8'))

# Sending gzipped data to KairosDB/Cassandra.
headers = {'content-type': 'application/gzip'}
requests.post("http://localhost:8080/api/v1/datapoints", data=gzipped, headers=headers)
print("Finished!")