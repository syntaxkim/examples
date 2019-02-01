from wsgiref.simple_server import make_server
from os import sys

def my_app(environ, start_response):

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    response = [b"This is a sample WSGI Application."]

    return response

if __name__ == "__main__":
    print("Strated WSGI Server on port 5000...")
    server = make_server('', 5000, my_app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)