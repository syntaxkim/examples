# How to Install and Secure Redis on Ubuntu 18.04
2019-01-21

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

## Installing and Configuring Redis
1. sudo apt update
2. sudo apt install redis-server
### Allow systemd to manage Redis as a service
3. sudo vi /etc/redis/redis.conf
(line 147, no -> systemd)
```
supervised systemd
```
4. sudo systemctl restart redis.service

## Testing Redis
1. sudo systemctl status redis
```
Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
```
* Redis is enabled meaning that it is set to start up every time the server boots.
* To disable automatic startup, run command: sudo systemctl disable redis

2. redis-cli
3. 127.0.0.1:6379> ping
```
PONG
```
4. 127.0.0.1:6379> set test "It's working!"
```
OK
```
5. 127.0.0.1:6379> get test
```
It's working!
```
6. 127.0.0.1:6379> exit
### Test if Redis is able to persist data even after it's been stopped or restarted.
7. sudo systemctl restart redis
8. redis-cli
9. 127.0.0.1:6379> get test
```
It's working!
```
10. 127.0.0.1:6379> exit

## Security Configuration
Redis' default configuration might be insecure so reconfiguring Redis is strongly recommended.
### Binding to localhost
By default, Redis is only accessible from localhost. But you need to make sure of it.
1. sudo vi /etc/redis/redis.conf
(On line 69, Uncomment the following line if it's commented (remove #))
```
bind 127.0.0.1 ::1
```
2. sudo systemctl restart redis
3. sudo netstat -lnp | grep redis
```
tcp    0  0 127.0.0.1:6379      0.0.0.0:*       LISTEN      4164/redis-server 1
tcp6   0  0 ::1:6379            :::*            LISTEN      4164/redis-server 1
```
* The output shows which host is bound to `redis-server`.

### Configuring a Redis Password
The following steps will force users to authenticate themselves.
1. openssl rand 60 | openssl base64 -A
(Generate a very long value)
```
some_sequence_number
```
2. sudo vi /etc/redis/redis.conf
(On line 500, SECURITY section, uncomment requirepass, set password)
```
requirepass some_sequence_number
```
3. sudo systemctl restart redis.service
4. redis-cli
5. 127.0.0.1:6379> set key1 10
```
(error) NOAUTH authentication required.
```
6. 127.0.0.1:6379> auth some_sequence_number
```
OK
```
7. Try setting the key and value again and see if it works.

### Renaming Dangerous Commands (LUSHDB, FLUSHALL, KEYS, PEXPIRE, ...)
1. sudo vi /etc/redis/redis.conf
(In SECURITY section)
```
# It is also possible to completely kill a command by renaming it into
# an empty string:
#
rename-command FLUSHDB ""
rename-command FLUSHALL ""
rename-command DEBUG ""
# Or rename a command:
rename-command SHUTDOWN SHUTDOWN_MENOT
rename-command CONFIG ASC12_CONFIG
```
* The best time to rename a command is when you're not using AOF persistence, or right after installation, that is, before your Redis-using application has been deployed.

## Disabling Protected Mode (for connecting from remote host)
1. sudo vi /etc/redis/redis.conf
(On line 88, yes -> no)
```
protected-mode no
```
2. sudo systemctl restart redis


## Log file
* sudo /var/log/reedis/redis-server.log