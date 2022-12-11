from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        with open('test.jpg', 'rb') as f:
            byte = f.read(1)
            while byte:
                self.wfile.write(byte)
                
        return
        