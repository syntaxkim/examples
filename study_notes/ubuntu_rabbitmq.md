(This note is not completed yet.)

# Installing on Ubuntu 18.04
2019-01-21

## Download from standard Ubuntu repositories. (Older version)
* sudo apt install rabbitmq-server
## Download the latest version.
* 
* sudo systemctl status rabbitmq-server

# Finding Configuration File
* sudo cat /var/log/rabbitmq/rabbit@apache.log (log file)
```
...
=INFO REPORT==== 21-Jan-2019::11:55:51 ===
node           : rabbit@apache
home dir       : /var/lib/rabbitmq
config file(s) : /etc/rabbitmq/rabbitmq.config (not found)
cookie hash    : SLA1mk6vz5F+TZgZBtNp6g==
log            : /var/log/rabbitmq/rabbit@apache.log
sasl log       : /var/log/rabbitmq/rabbit@apache-sasl.log
database dir   : /var/lib/rabbitmq/mnesia/rabbit@apache
...
```

## Allowing "guest" user to connect from a remote host. (Not recommended on production)
1. sudo vi /etc/rabbitmq/rabbitmq.config
```
## The default "guest" user is only permitted to access the server
## via a loopback interface (e.g. localhost).
[
        {rabbit, [
                {loopback_users, none}
                ]
        }
].
```

2. sudo systemctl restart rabbitmq-server.service
