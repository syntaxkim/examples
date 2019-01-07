from http.server import HTTPServer, BaseHTTPRequestHandler
from os import sys

'''Warning:
http.server is not recommended for production. It only implements basic security checks.
'''


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    server = HTTPServer(('', 5000), MyHandler)
    print("Started WebServer on port 5000...")
    print("Press ^C to quit WebServer.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
    