#!/bin/sh

# Declaring default values for some needed variables
database_name='scadabr'
database_username='root'
database_password=''

chmod +x export_scadabr_database_to_kairosdb.py

# Clear the console
clear
clear
clear

# Asking for the user credentials
printf "================= ScadaBR_to_KairosDB v0.1 =================\n\n"
printf "  Check out the official repository at\n" 
printf "  https://github.com/paladini/ScadaBR_to_KairosDB\n"
printf "\n"
printf "  # Default values:\n"
printf "  Database name    --> \"scadabr\"\n"
printf "  Username (login) --> \"root\"\n"
printf "  Password (login) --> \"\"\n"
printf "\n\n  Please, make sure that MySQL/MariaDB server, Cassandra and"
printf "\n  KairosDB are running in your PC before execute this script."
printf "\n\n"
printf "=============================================================\n"
printf "\n"
read -e -p "(a) Database name to export: " -i "scadabr" DATABASE_NAME
read -e -p "(b) Username for $DATABASE_NAME: " -i "root" DATABASE_USERNAME
read -e -p "(c) Password for $DATABASE_USERNAME: " -i "" DATABASE_PASSWORD
printf "\n=============================================================\n"
printf "\nStarting to export NOW!\n"
printf "\n"
echo -ne '#############                     (33%)\r'
sleep 0.2
echo -ne '################################             (66%)\r'
sleep 0.2
echo -ne '#######################################################   (100%)\r'
echo -ne '\n\n'

# Running python script with these arguments
./scadabr_database_to_kairosdb.py $DATABASE_NAME $DATABASE_USERNAME $DATABASE_PASSWORD