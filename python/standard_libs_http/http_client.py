from http.client import HTTPConnection
from urllib.parse import urlencode

def connect(method, url='/', body={}, headers={}):
    print(f'________method: {method}________')

    conn = HTTPConnection(host)
    conn.request(method, url, body, headers)
    res = conn.getresponse()
    data = res.read()

    print(res.status, res.reason)
    print(res.msg)
    try:
        charset = res.msg.get_param('charset')
        print(data.decode(charset))
    except:
        # If no charset in header
        print(data.decode())

    print('Body length:', len(data))
    print("data == b: ", data == b'')

    conn.close()
    print('________connection closed________\n')

if __name__ == "__main__":
    host = '127.0.0.1:5000'

    # GET request
    connect('GET')

    # HEAD request
    connect('HEAD')
    
    body = urlencode({
        'name': 'Minsu',
    })
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain',
    }

    # POST request
    connect('POST', '/', body, headers)

    # PUT request (will return 405 METHOD NOW ALLOWED)
    connect('PUT', '/', body, headers)
