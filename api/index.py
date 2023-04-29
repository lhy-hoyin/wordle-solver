import os
from http.server import BaseHTTPRequestHandler

from .solver.wordle_bot import main

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Wordle Bot is online'.encode('utf-8'))

        main()        

        return        
    
if __name__ == "__main__":
    main()
