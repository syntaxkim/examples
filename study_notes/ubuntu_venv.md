# How to Use venv on Ubuntu 18.04
2018-12-16

## Installing the Latest Version of Python
Ubuntu 18.04 ships with Python 3.6 by default, but in most linux distributions command 'python' calls Python 2. (Python 3 will be the default in the future.)
So, using 'python3/pip3' command is recommended for now to call Python 3/pip3.
1. sudo apt install python3.7

## Setting up a Specific Version as Default Python (Optional)
1. sudo vi /home/ubuntu/.bashrc
alias python='python3.7'

## Installing pip for Python 3
Pip is not installed by default on Ubuntu 18.04.
1. sudo apt install python3-pip
2. sudo reboot
3. pip3 --version

## Installing packages (Only if there is no package available through the apt package manager)
1. pip3 install package

## Setting up Python Virtual Environment (Python 3)
1. (If pip3 is not installed) sudo apt install python3-pip
### Installing virtualenv by Using apt (Recommended as they are tested to work properly on Ubuntu systems)
2. sudo apt install python3-venv
3. python3 -m venv venv
### Installing virtualenv by using pip3 (Only if there is no package available through the package manager)
2. sudo pip3 install virtualenv
3. sudo virtualenv venv

### In most cases you should use pip within a virtual environments only. 
4. source venv/bin/activate
The virtual environment’s bin directory will be added at the beginning of the $PATH variable.
Within the virtual environment, you can use the command pip instead of pip3 and python instead of python3.
5. pip install gunicorn (or -r requirements.txt)
6. deactivate
7. which gunicorn

## cpvirtualenv
* cpvirtualenv ENVNAME TARGETENVNAME (Duplicate an existing virtualenv environment)
**Warning**
Copying virtual environments is not well supported. Each virtualenv has path information hard-coded into it, and there may be cases where the copy code does not know it needs to update a particular file. Use with caution.