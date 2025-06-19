#!/usr/bin/env python3
"""
Test square symbols for revenue
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
    
    with socketserver.TCPServer(("", 8011), Handler) as httpd:
        print("🟪 Testing Square Symbols at http://localhost:8011")
        print("🐛 Debug: http://localhost:8011/debug_revenue_map.html")
        print("📊 Dashboard: http://localhost:8011/brazil_delivery_revenue_dashboard.html")
        print("\n🔍 Purple squares should now be visible on the map")
        print("   Larger squares = higher revenue")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8011/debug_revenue_map.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()