from http.server import BaseHTTPRequestHandler
from urllib import parse
import shutil

from solver.wordle_bot import main

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        main()        
        
if __name__ == "__main__":
    main()