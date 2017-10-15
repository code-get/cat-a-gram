#!/bin/bash
# cat-a-gram-model
# MySQL Startup Script
# by: Christopher Landry
# date: 14-Oct-2017

# Swap placeholder values with environment vars
sqlcmd_createuser="CREATE USER $PGSQL_DB_USERNAME WITH NOCREATEDB NOCREATEROLE NOSUPERUSER ENCRYPTED PASSWORD '$PGSQL_DB_USER_PASSWORD';"
sqlcmd_createdb="CREATE DATABASE $PGSQL_DB_NAME WITH OWNER $PGSQL_DB_USERNAME;"

# Run the database setup script
/usr/bin/pg_ctl start -D /var/lib/pgsql/data
sleep 10

psql --command "$sqlcmd_createuser"
psql --command "$sqlcmd_createdb"

# So that others can't get this value so easily
unset PGSQL_DB_USER_PASSWORD
