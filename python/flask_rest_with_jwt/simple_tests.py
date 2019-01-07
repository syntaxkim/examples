import unittest
import requests

class Tests(unittest.TestCase):

    def test_1(self):
        """Check login"""
        self.assertTrue(login(path='/login'))

    def test_2(self):
        """Check false login"""
        self.assertFalse(login(path='/login', password="wrong password"))

    def test_3(self):
        """Check users"""
        self.assertTrue(users())

    def test_4(self):
        """Check get_tasks"""
        self.assertTrue(tasks())


url = 'http://127.0.0.1:5000'
username = 'admin'
password = 'password'

def connect(f):
    def inner():
        r = requests.get(url+'/login', auth=(username, password))
    
        if r.status_code != 200:
            return False

        if not 'token' in r.json():
            return False

        headers = {'x-access-token': r.json()['token']}

        return f(headers)

    return inner

def login(path, username=username, password=password):
    r = requests.get(url+path, auth=(username, password))

    if r.status_code != 200:
        return False

    if not 'token' in r.json():
        return False

    return True

@connect
def users(headers={}):
    r = requests.get(url+'/users', headers=headers)

    if r.status_code != 200:
        return False
    
    return True

@connect
def tasks(headers={}):
    r = requests.get(url+'/tasks', headers=headers)

    if r.status_code != 200:
        return False
    
    return True

if __name__ == "__main__":
    unittest.main()