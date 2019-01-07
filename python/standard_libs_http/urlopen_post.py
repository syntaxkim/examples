from urllib.request import urlopen

'''
This program sends a POST request to the local server.
Before run this file, make sure to run application.py.
Type your name, the Flask app will greet you.
If not, the Flask server asks you who you are.
Content-Length in header will vary by your input length.
'''

name = input("Client: Your name? ")
data = f"name={name}"

f = urlopen("http://127.0.0.1:5000", bytes(data, encoding='utf-8'))

print("________________________________")
print(f.info())
print('Server: ' + f.read().decode('utf-8'))