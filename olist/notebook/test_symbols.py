#!/usr/bin/env python3
"""
Test which symbols work with Plotly mapbox
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
    
    with socketserver.TCPServer(("", 8010), Handler) as httpd:
        print("🔺 Testing Triangle Symbols at http://localhost:8010")
        print("🐛 Debug: http://localhost:8010/debug_revenue_map.html")
        print("📊 Dashboard: http://localhost:8010/brazil_delivery_revenue_dashboard.html")
        print("\n🔍 Check if triangles are now visible on the map")
        print("   Purple triangles should represent revenue data")
        print("   Larger triangles = higher revenue")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8010/debug_revenue_map.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()