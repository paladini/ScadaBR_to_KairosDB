#!/usr/bin/env python3
import requests
import gzip
import json
import sys
import pymysql as mariadb

# Creating the connection with MySQL/MariaDB database. 
# 
# Attributes:
#   sys.argv[1] = database name, that was sent by the caller script.
#   sys.argv[2] = username of the MySQL/MariaDB server.
#   sys.argv[3] = if has a sys.argv[3], then use it. Otherwise the password is blank/empty.
#
passwd = '' if (len(sys.argv) <= 3) else sys.argv[3]
mariadb_connection = mariadb.connect(user=sys.argv[2],passwd=passwd, database=sys.argv[1])
cursor = mariadb_connection.cursor()

# Execute a SQL query on the MySQL/MariaDB database.
def execute_query(query):
    try:
        cursor.execute(query)
        return cursor
    except mariadb.Error as error:
        print("[ERROR] {}".format(error))

print("For comparison purposes, we've waited for about 15 minutes to export 1.7 million point values in a low-end notebook.")

# Querying all data (format: <sensor name>, <dataType>, <measured value>, <timestamp in UNIX format> )
dataPoints = execute_query("SELECT * FROM dataPoints;").fetchall()
print("Number of data points detected: %u.\n" % len(dataPoints))
for dp in dataPoints:

    # We should connect for every data point because this way we avoid a lot of errors/exceptions of timeout.
    cursor = mariadb.connect(user=sys.argv[2],passwd=passwd, database=sys.argv[1]).cursor()

    # Creating structured data in KairosDB format
    data = []
    send = {
        "name": dp[1],
        "tags": {
            "sensor_name": dp[1]
        }
    }

    # Parsing point values in KairosDB format ( [[<timestamp1>, <value1>], [<timestamp2>, <value2>], ... [<timestampN>, <valueN>]] )
    pointValues = execute_query("SELECT dataType, pointValue, ts FROM pointValues WHERE dataPointId='%u';" % dp[0])
    for pv in pointValues:
        data.append([pv[2], pv[1]])
    send["datapoints"] = data

    print("\t[STATUS] Exporting %u point values from %s." % (pointValues.rowcount, dp[1]))
    print("\t[STATUS] Sending data to KairosDB. This may take some minutes...")

    # Gzipping json before send.
    gzipped = gzip.compress(bytes(json.dumps(send), 'UTF-8'))

    # Sending gzipped data to KairosDB/Cassandra.
    headers = {'content-type': 'application/gzip'}
    requests.post("http://localhost:8080/api/v1/datapoints", data=gzipped, headers=headers)
    print("\t[STATUS] %u values from data point %s has sent to KairosDB." % (pointValues.rowcount, dp[1]))

print("\n[STATUS] Finished!\n")
