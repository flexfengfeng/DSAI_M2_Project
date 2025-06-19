#!/usr/bin/env python3
"""
Test the revenue dashboard with proper diamond sizing
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
    
    with socketserver.TCPServer(("", 8006), Handler) as httpd:
        print("🚀 Revenue Dashboard (Fixed) running at http://localhost:8006")
        print("📊 URL: http://localhost:8006/brazil_delivery_revenue_dashboard.html")
        print("\n✅ Fixed Issues:")
        print("   💎 Diamond size now properly scales with revenue (R$ 187 - R$ 24,846)")
        print("   📏 Size range: 8.2 - 32.8 pixels based on revenue amount")
        print("   💜 Purple diamonds clearly visible on map")
        print("   🎯 Revenue view shows all diamonds by default")
        print("\n💡 Usage:")
        print("   • Click 'Revenue View' to see purple diamonds sized by revenue")
        print("   • Use state/city filters to focus on specific regions")
        print("   • Larger diamonds = higher revenue for that ZIP code")
        print("\n⏹️  Press Ctrl+C to stop")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8006/brazil_delivery_revenue_dashboard.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()