Export ScadaBR database to KairosDB
=======================

If you're running ScadaBR and you would like to export your MySQL/MariaDB database to KairosDB, a modern NoSQL time series database that runs on top of Cassandra, then you're in the right place. 

Installation / How to use? 
---------------

It's very simple to use this script and it should work in any Linux distribution that has Python3 installed and [mysql-connector-python](https://dev.mysql.com/downloads/connector/python/2.1.html) [both are pre-requisite, please install mysql-connector-python].

Before start make sure that you are okay with all of the following items:

- MySQL/MariaDB server up and running.
- KairosDB server up and running.
- ScadaBR database inside your server.

To run this script execute the following commands in your Terminal (Ctrl+Alt+T):

```sh
chmod +x export.sh
./export.sh
```

The script will ask you to provide some informations:

**The dabase name:** the ScadaBR database name. The default is `scadabr`.
**MySQL/MariaDB username:** give the username you use to connect into to MySQL/MariaDB. The default is `root`.
**MySQL/MariaDB password:** give the password you use WITH THE USERNAME PROVIDED PREVIOUSLY to connect to MySQL/MariaDB. The default is `` (empty).

Troubles? Suggestions? Questions?
--------------

Please, contact me if you need any help with troubles, questions or do you have some suggestions to this script.

fernandopalad at gmail.com

About
--------------

This small script was developed by Fernando Paladini on 2015. Hope it help you :) 