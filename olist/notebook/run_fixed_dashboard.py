#!/usr/bin/env python3
"""
Run the fixed dashboard with visible diamonds
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
    
    with socketserver.TCPServer(("", 8008), Handler) as httpd:
        print("💎 Fixed Diamond Dashboard at http://localhost:8008")
        print("📊 URL: http://localhost:8008/brazil_delivery_revenue_dashboard.html")
        print("\n✅ Fixes Applied:")
        print("   💎 Diamonds now visible on map (not just legend)")
        print("   📏 Larger size range: 10-40px for better visibility")
        print("   🎯 Filtered out zero revenue data for cleaner view")
        print("   💜 Purple diamonds with dark purple borders")
        print("   📍 Slight offset in dual view to avoid overlap")
        print("\n💡 Instructions:")
        print("   1. Click 'Revenue View' button")
        print("   2. Look for purple diamond shapes on the map")
        print("   3. Larger diamonds = higher revenue")
        print("   4. Use filters to focus on specific regions")
        print("\n⏹️  Press Ctrl+C to stop")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8008/brazil_delivery_revenue_dashboard.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()