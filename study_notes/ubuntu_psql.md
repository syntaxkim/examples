# How to Install PostgreSQL on Ubuntu 18.04 
2018-10-01

* [ubuntu doc](https://help.ubuntu.com/lts/serverguide/postgresql.html.en)
* [postgresql doc](https://www.postgresql.org/docs/10/static/admin.html)

## Installing PostgreSQL
[postgresql doc](https://www.postgresql.org/docs/10/static/runtime-config-connection.html)
sudo apt install postgresql

## enable other computers to connect to your PostgreSQL server
sudo vi /etc/postgresql/10/main/postgresql.conf
listen_addresses = '*'

[reference](https://www.postgresql.org/docs/10/static/app-psql.html)
## set a password for the user 'postgres'
sudo -u postgres psql
## This command prompts for the new password, encrypts it, and sends it to the server as an ALTER ROLE command.
\password [ username or current user by default ]
(set a password)
\q

[reference](https://www.postgresql.org/docs/10/static/auth-pg-hba-conf.html)
## add postgres user into the entry list
sudo vi /etc/postgresql/10/main/pg_hba.conf
```
host	all	postgres	192.168.111.1/24	md5
```

## restart postgresql service
sudo systemctl restart postgresql

## open port (if port number is 5432)
sudo ufw allow 5432/tcp

# on windows-client side
# connect to a 'lecture' database at server with a user name 'postgres'
# if not specifed, default port number is 5432 or environment variable 'PGPORT'
# other environment variable: PGDATABASE, PGHOST, PGUSER
[URI method](https://www.postgresql.org/docs/10/static/libpq-connect.html#LIBPQ-CONNSTRING)
psql postgresql://postgres@192.168.111.200:5432/lecture
# arguments method
psql -U postgres -h 192.168.111.200 -p 5432 -d lecture

## Avoid regulary having to type in passwords
[pgpass](https://www.postgresql.org/docs/10/static/libpq-pgpass.html)

## Other commands
* \l = list of databases
* \d = list of tables
* \d (table name) = show table information
* \c = database and user name
* \c (database name) = change to database