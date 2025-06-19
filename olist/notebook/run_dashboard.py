#!/usr/bin/env python3
"""
Simple script to run the dashboard with proper debugging
"""
import http.server
import socketserver
import webbrowser
import os
import threading
import time

def start_server():
    os.chdir('/Users/fengfeng/Dev/DSAI_M2_Project/olist/notebook')
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
    
    with socketserver.TCPServer(("", 8002), Handler) as httpd:
        print("🚀 Server running at http://localhost:8002")
        print("📊 Fixed Dashboard: http://localhost:8002/brazil_delivery_dashboard_fixed.html")
        print("🔧 Debug Page: http://localhost:8002/brazil_delivery_dashboard_debug.html")
        print("📄 Test Page: http://localhost:8002/test_dashboard.html")
        print("\n🔍 Check browser console for debug messages")
        print("📋 Page title will show data source and average")
        print("\n⏹️  Press Ctrl+C to stop")
        
        # Auto-open the fixed dashboard
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8002/brazil_delivery_dashboard_fixed.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()