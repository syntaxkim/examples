# How to Set Up Ubuntu
2018-12-16

## Setting Up Static IP (Optional)
1. sudo vi /etc/netplan/01-config.ymal (or 50-cloud-init.yaml)
```
network:
        version: 2
        renderer: networkd
        ethernets:
                ens32:
                        addresses: [192.168.111.200/24]
                        gateway4: 192.168.111.2
                        nameservers:
                                search: [mydomain]
                                addresses: [192.168.111.2]
```
2. sudo netplan apply

## Setting Up DNS
1. sudo vi /etc/systemd/resolved.conf
```
DNS=8.8.8.8
```
2. sudo systemctl restart systemd-resolved

## Adding universe repository
1. sudo apt-add-repository universe

## Updating Packages
sudo apt update && sudo apt upgrade

## Installing Some Handy Network Tools (optional)
1. sudo apt install netcat-openbsd tcpdump traceroute mtr nmap

## Delete all unnecessary dependencies.
sudo apt autoremove

## Adding a New User (optional)

## Setting Up SSH

## Setting Up UFW(firewall).

## Installing Python (optional)
1. sudo apt install python3-pip python3-venv