from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message="Hello World"
        self.wfile.write(open(join('img','wordle-solver-light.jpg'), 'rb'))
        return
        