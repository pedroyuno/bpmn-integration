#!/usr/bin/env python3
"""
Simple HTTP server to serve BPMN viewer locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local file access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 BPMN Viewer Server starting...")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🌐 Open your browser and navigate to: http://localhost:{PORT}/bpmn_viewer.html")
        print(f"📊 Your BPMN diagram will load automatically!")
        print(f"🛑 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Try to open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}/bpmn_viewer.html')
            print("✅ Browser opened automatically")
        except:
            print("ℹ️  Could not open browser automatically")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped. Goodbye!")

if __name__ == "__main__":
    main() 