Export ScadaBR database to KairosDB
=======================

If you're running ScadaBR and you would like to export your MySQL/MariaDB database to KairosDB, a modern NoSQL time series database that runs on top of Cassandra, then you're in the right place.

This small Python script will easily convert your ScadaBR database into a KairosDB database.

Installation / How to use? 
---------------

It's very simple to use this script and it should work in any Linux distribution. However, we've the following prerequisites: 

* Any version of Python 3 installed.
* [pip3](http://pip.readthedocs.org/en/stable/), the Python package manager for Python 3.
* [mysql-connector-python](https://dev.mysql.com/downloads/connector/python/) (don't forget, download the version for Python3).

In order to run the script correctly, please provide both requisites in your machine.

**1) Before start make sure that you are okay with all of the following items:**

1. MySQL/MariaDB server up and running.
2. KairosDB server up and running.
3. ScadaBR database inside your server.

**2) Run the script in your Terminal (Ctrl+Alt+T):**

```sh
chmod +x export.sh
./export.sh
```

**3) Provide the credentials:**

In order to export the database, our Python script must know your database name, your username and your password for MySQL/MariaDB database.  

- Dabase name: the ScadaBR database name. The default is `scadabr`.
- Username: give the username you use to connect into to MySQL/MariaDB. The default is `root`.
- Password: give the password you use WITH THE USERNAME PROVIDED PREVIOUSLY to connect to MySQL/MariaDB. The default is `` (empty).

Now the script should do the work! Be patient and if you got any trouble, question, bug or want to suggest us a feature, feel free to contact me at fernandopalad@gmail.com (or via GitHub Issues).

About
--------------

This small script was developed by Fernando Paladini on 2015. Hope it help you :) 
