# How to Install MySQL on Ubuntu 18.04
2019-01-26

## Installing MySQL
### from Ubuntu Repository (5.7)
1. sudo apt update
2. sudo apt install mysql-server
### from MySQL Repository by Adding MySQL Repository (8.0, The latest version)
1. Go to [mysql.com](https://www.mysql.com/) -> DOWNLOADS -> Community -> MySQL APT Repository -> Download
2. Right click `No thanks, just start my download.`, Copy link address.
3. cd /tmp
4. curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
* -O: Output to a file instead of standard output.
* -L: Follow HTTP redirects.
5. sudo dpkg -i mysql-apt-config*
* -i: Install specified file.
6. OK
7. sudo apt update
8. rm mysql-apt-config*
9. sudo apt install mysql-server

## Configuring MySQL
1. sudo mysql_secure_installation
2. sudo mysql
3. mysql> CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
4. mysql> GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

## Testing MySQL
1. sudo systemctl status mysql.service
```
Active: active (running)
```
2. sudo mysqladmin -u root version (connect to MySQL as root (-u root) and return the version.)

### Configuring Default Authentication
* sudo vi /etc/mysql/mysql.conf.d/default-auth-override.cnf
* default_authentication_plugin server setting
* /etc/mysql/mysql.conf.d/mysqld.cnf
```
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
```