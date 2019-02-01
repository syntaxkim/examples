# How to set up SSH
2018-10-02

**Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.**
**SSH server is not installed by default in Ubuntu systems but it can be easily installed from the main Ubuntu repositories.**

## Installing OpenSSH server (might be pre-installed)
1. sudo apt update
2. sudo apt install openssh-server
3. sudo apt enable ssh

## open port 22
4. sudo ufw allow 22/tcp

## Connect to ssh server from client-side
5. ssh <username>@<ipaddress>

## Managing SSH Service
* sudo systemctl status/start/restart/stop/disable/enable ssh
* stop: stop the program but autostart during system boot
* enable: autostart during system boot
* disable: do not start during system boot