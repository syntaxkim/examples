# How to set up UFW
2018-12-21

**Uncomplicated Firewall (UFW) is a program for managing a netfilter firewall designed to be easy to use.**

1. sudo ufw status
Ubuntu comes with a firewall pre-installed called ufw which is inactive by default.

2. sudo ufw default deny incoming
Blocking all incoming requests is a good practice as it makes it much easier to manage your rules.

3. sudo ufw default allow outgoing
We can also establish a default rule for our outgoing connections.
If you turn it to active at this moment, SSH will no longer be able to communicate with the server. And it is time to establish our own ports settings. Let’s open SSH first.

4. sudo ufw allow ssh

5. sudo ufw allow http (same as sudo ufw allow 80/tcp)
* (For vagarant) sudo ufw allow 2222/tcp (Allow all TCP connections through port 2222)

6. sudo ufw allow https (Same s sudo ufw allow 443/https)

7. sudo ufw enable
Be aware that you could lose your SSH connection to your server if you didn’t appropriately allow port for SSH. Some cloud providers do offer a way to regain access to your system through an external control panel.

8. sudo ufw allow 8000 (Optional, for test purpose of django)

### Other commands
- sudo ufw status verbose
- sudo ufw app list (List application profiles)
- sudo ufw app info 'Nginx HTTP'
- sudo ufw allow 'Nginx HTTPS'
- sudo ufw disable
- sudo ufw allow from 64.63.62.61
- sudo ufw allow from 64.63.62.61 to any port 80
- sudo ufw deny from 64.63.62.61
- sudo ufw deny from 64.63.62.61 to any port 443
- sudo ufw reset (Reset UFW will disable UFW, and delete all active rules.)
- sudo ufw status numbered
- sudo ufw delete 2
