#!/bin/bash
# cat-a-gram-model
# MySQL Startup Script
# by: Christopher Landry
# date: 14-Oct-2017

# Swap placeholder values with environment vars
sqlcmd_createuser="CREATE USER $PGSQL_DB_USERNAME WITH NOCREATEDB NOCREATEROLE NOSUPERUSER ENCRYPTED PASSWORD '$PGSQL_DB_USER_PASSWORD';"
sqlcmd_createdb="CREATE DATABASE $PGSQL_DB_NAME WITH OWNER $PGSQL_DB_USERNAME;"
sqlcmd_createtable="CREATE TABLE image (id varchar(10) PRIMARY KEY, url text, source_url text);"

# Run the database setup script
/usr/bin/pg_ctl start -D /var/lib/pgsql/data
sleep 10

psql --command "$sqlcmd_createuser"
psql --command "$sqlcmd_createdb"
export PGPASSWORD=$PGSQL_DB_USER_PASSWORD
psql $PGSQL_DB_NAME -U $PGSQL_DB_USERNAME --command "$sqlcmd_createtable" -w

# So that others can't get this value so easily
unset PGSQL_DB_USER_PASSWORD
