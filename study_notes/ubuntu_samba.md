# How to Install Samba on Ubuntu 18.04
2018-10-02

## Installing samba server
sudo apt install samba

## create a shared foler
mkdir /home/<username>/share

## (optional) change permissions as needed
sudo chmod 707 /share/

## open the configuration file
sudo vi /etc/samba/smb.conf
## add the following lines at the bottom of the file
```
[share]
    comment = Samaba on Ubuntu
    path = /home/<username>/share
    read only = no
    browsable = yes
```

## (optional) limit which IP address from which can be connected
## under [global] section, add
hosts allow = 127.0.0.1, <IP address>
hosts deny = 0.0.0.0/0

## add a user who can access share with the password
sudo smbpasswd -a <username>

## restart the service
sudo systemctl restart smbd

3# open port
sudo ufw allow 445/tcp

## on Windows (client side)
`\\<server-address>\share`
