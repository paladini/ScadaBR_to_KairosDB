! Export ScadaBR database to KairosDB
=======================

If you're running ScadaBR and you would like to export your MySQL/MariaDB database to KairosDB (non-sql and time series database) then you're in the right place. 

Installation / How to use? 
---------------

You don't need to install anything, it's very simple to use this script and it should work in any Linux distribution that has Python2 or Python3 installed.

Before start make sure that you are okay with all of the following items:

- MySQL/MariaDB server up and running.
- KairosDB server up and running.
- ScadaBR database inside your server.

To run this script, just double-click "run.sh" or execute the following command in your Terminal (Ctrl+Alt+T):

```sh
chmod +x run.sh
./run.sh
```

**The script will ask you to provide some informations:**

1. **The dabase name:** the ScadaBR database name. The default is `scadabr`.
2. **MySQL/MariaDB username:** give the username you use to connect into to MySQL/MariaDB. The default is `root`.
3.  **MySQL/MariaDB password:** give the password you use WITH THE USERNAME PROVIDED PREVIOUSLY to connect to MySQL/MariaDB. The default is `` (empty).


Troubles? Suggestions? Questions?
--------------

Please, contact me if you need any help with troubles, questions or do you have some suggestions to this script.

fernandopalad at gmail.com