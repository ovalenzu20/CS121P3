'''
Created on May 30, 2019

@author: omarvalenzuela
'''
from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def _set_json_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
    def do_GET(self):
        pass
        
    