from http.server import BaseHTTPRequestHandler
from urllib import parse
import shutil

from solver.wordle_bot import main

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','image/jpg')
        self.end_headers()

        self.wfile.write("hello world".encode())

        #with open('test.jpg', 'rb') as f:
        #    bytes=f.read(1)
        #    while bytes:
        #        self.wfile.write(bytes)
                
        with open('test.jpg', 'rb') as content:
            shutil.copyfileobj(content, self.wfile)
                
        return
        
    def run():
        main()
        
if __name__ == "__main__":
    main()