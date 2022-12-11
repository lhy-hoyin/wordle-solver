from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','image.jpeg')
        self.end_headers()

        self.wfile.write("hello world".encode())

        with open('test.jpg', 'rb') as f:
            self.wfile.write(f.read(-1))
                
        return
        