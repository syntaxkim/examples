# How to Use ssh-keygen on a Local Machine
2018-12-21

[Lecture](https://www.udacity.com/course/configuring-linux-web-servers--ud299)

1. (local) ssh-keygen (Generate a key pair using an application called ssh-keygen.)
When it’s done, ssh-keygen has generated two files(id_rsa, id_rsa.pub) and ‘rsa.pub’ is what we’ll place on our server to enable key based authentication. The type of key to be generated is specified with -t option. if invoked without any arguments, ssh-keygen will generate on RSA key for usein SSH protocol 2 connections. Run command 'man ssh-keygen' for more detail.

2. (server, at home directory) mkdir .ssh
This is a special directory where all of your key related files must be stored.

3. touch .ssh/authorized_keys
This is another special file that will store all of the public keys that this account is allowed to use for authentication, with one key per line in that file.

4. (local) cat .ssh/id_rsa.pub
Copy the content of this .pub file.

5. (server) vi .ssh/authorized_keys
Paste the line here.

6. chmod 700 .ssh

7. chmod 644(or 600) .ssh/authorized_keys
Set up some specific file permissions on the authorized key file and the SSH directory. This is a security measure that other users cannot gain access to your account.

8. (local) ssh ubuntu@192.168.111.200 -i ~/.ssh/id_rsa
Now log in with your private key. If you set a passphrase for your key pair, you’ll be asked to enter that.

9. (server) sudo vi /etc/ssh/sshd_config
Open a configuration file for sshd which is the service that’s running on the server listening for all of your SSH connections.

10. Find and edit the line #PasswordAuthentication yes to PasswordAuthentication no
Disable the password base logins. This will force all of your users to only be able to login using a key pair.

11. sudo systemctl restart ssh
Restart the sshd service as it only reads its configuration file when it’s initially started up. Now all users will be forced to log in using a key pair.

## default arguments of -i option when using ssh
~/.ssh/id_dsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ed25519 and ~/.ssh/id_rsa 

## One-step command to copy public key from local to server
scp ~/.ssh/id_rsa.pub ubuntu@192.168.111.200:~/.ssh/authorized_keys