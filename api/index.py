from http.server import BaseHTTPRequestHandler
from urllib import parse



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message="Hello World"
        
        START_PHOTO_PATH = './img/wordle-solver-light.jpg'
        
        self.wfile.write(open(START_PHOTO_PATH))
        return
        