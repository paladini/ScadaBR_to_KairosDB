#!/bin/python3.4
import requests
import gzip
import json
import sys
import mysql.connector as mariadb

# Creating the connection with MySQL/MariaDB database. 
# 
# Attributes:
# 	sys.argv[1] = database name, that was sent by the caller script.
# 	sys.argv[2] = username of the MySQL/MariaDB server.
# 	sys.argv[3] = if has a sys.argv[3], then use it. Otherwise the password is blank/empty.
#
passwd = '' if (len(sys.argv) <= 3) else sys.argv[3]
mariadb_connection = mariadb.connect(user=sys.argv[2],password=passwd, database=sys.argv[1])
cursor = mariadb_connection.cursor()

# Execute a SQL query on the MySQL/MariaDB database.
def execute_query(query):
	try:
		cursor.execute(query)
		return cursor
	except mariadb.Error as error:
		print("[ERROR] {}".format(error))

# Querying all data (format: <sensor name>, <dataType>, <measured value>, <timestamp in UNIX format> )
query = execute_query("SELECT dataPoints.xid, pointValues.dataType, \
						pointValues.pointValue, pointValues.ts from pointValues \
						INNER JOIN dataPoints on \
						pointValues.dataPointId=dataPoints.id")

# Parsing structured data to KairosDB format
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

print("[STATUS] Data to be exported: " + str(len(send_to_kairos)) + " point values.")
print("[STATUS] Sending data to KairosDB...\n\nDepending on how many data you have sent, this may take some minutes.")
print("\n  For comparison purposes, we've waited for about 15 minutes to export\n  1.7 million point values in a low-end notebook.")

# Gzipping json before send.
gzipped = gzip.compress(bytes(json.dumps(send_to_kairos), 'UTF-8'))

# Sending gzipped data to KairosDB/Cassandra.
headers = {'content-type': 'application/gzip'}
requests.post("http://localhost:8080/api/v1/datapoints", data=gzipped, headers=headers)
print("\n[STATUS] Finished!\n")