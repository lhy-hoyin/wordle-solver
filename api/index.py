from http.server import BaseHTTPRequestHandler
from urllib import parse
import shutil

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','image/jpeg')
        self.end_headers()

        self.wfile.write("hello world".encode())

        #with open('test.jpg', 'rb') as f:
        #    bytes=f.read(1)
        #    while bytes:
        #        self.wfile.write(bytes)
                
        with open('test.jpg', 'rb') as content:
            shutil.copyfileobj(content, self.wfile)
                
        return
        