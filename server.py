#!/usr/bin/env python3
"""
Simple HTTP Server for the IoT Security Dashboard Website
Run this script to serve the website locally
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Set the directory containing your website files
WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))

# Change to the website directory
os.chdir(WEBSITE_DIR)
print(f"Serving from directory: {WEBSITE_DIR}")

# Default port
PORT = 8000

# Custom request handler to handle directory paths
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Handle directory paths by serving index.html
    def do_GET(self):
        # Check if path ends with /
        if self.path.endswith('/'):
            self.path = os.path.join(self.path, 'index.html')
        # Check if PDF is being served from parent directory
        if self.path.startswith('/output/') and not os.path.exists(self.path[1:]):
            # Adjust path to serve from parent directory
            parent_dir = str(Path(WEBSITE_DIR).parent)
            full_path = os.path.join(parent_dir, self.path[1:])
            if os.path.exists(full_path):
                with open(full_path, 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/pdf')
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
        # Otherwise, use the default handler
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server(port=PORT):
    handler = MyHTTPRequestHandler
    
    # Attempt to start server
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Server started at http://localhost:{port}")
            print("To view the website, open a browser and navigate to:")
            print(f"http://localhost:{port}/")
            print("Press Ctrl+C to stop the server.")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{port}/')
            
            # Start server
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Port {port} is already in use. Trying port {port+1}...")
            run_server(port+1)
        else:
            raise

if __name__ == "__main__":
    run_server() 