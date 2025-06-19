#!/usr/bin/env python3
"""
Test diamond symbols
"""
import http.server
import socketserver
import webbrowser
import os
import threading

def start_server():
    os.chdir('/Users/fengfeng/Dev/DSAI_M2_Project/olist/notebook')
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
    
    with socketserver.TCPServer(("", 8007), Handler) as httpd:
        print("🔷 Diamond Symbol Test at http://localhost:8007")
        print("📊 Test: http://localhost:8007/test_diamond_symbols.html")
        print("📊 Dashboard: http://localhost:8007/brazil_delivery_revenue_dashboard.html")
        print("\n🔍 Check if diamonds are visible on both pages")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8007/test_diamond_symbols.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()