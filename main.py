#!/usr/bin/env python3

import http.server
import socketserver
import json
import os
from datetime import datetime
from urllib.parse import urlparse

print("Script start")

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()
    
    def do_POST(self):
        self.handle_request()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()
    
    def handle_request(self):
        dt = datetime.now()
        version = os.environ.get("SF_TAG", "latest")
        
        client_ip = self.client_address[0]
        print(f"Request received: {self.command} {self.path} from {client_ip}")
        
        response_data = {
            "message": "Hello from python",
            "dt": dt.isoformat(),
            "version": version
        }
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_cors_headers()
        self.end_headers()
        
        self.wfile.write(json.dumps(response_data).encode("utf-8"))
    
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

PORT = 3000
HOST = "0.0.0.0"

print("Server created")

with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
    print("Server listening callback")
    print(f"Server running on {HOST}:{PORT}")
    httpd.serve_forever()
