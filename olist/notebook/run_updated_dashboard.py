#!/usr/bin/env python3
"""
Run the updated delivery time & revenue dashboard with filters
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
    
    with socketserver.TCPServer(("", 8005), Handler) as httpd:
        print("🚀 Updated Dashboard running at http://localhost:8005")
        print("📊 URL: http://localhost:8005/brazil_delivery_revenue_dashboard.html")
        print("\n✨ New Features:")
        print("   🗺️  Three-column layout with filters on both sides")
        print("   🏛️  State & City filters on the right panel")
        print("   💜 Purple diamond markers for revenue data")
        print("   🔄 Real-time filtering affects all visualizations")
        print("   📊 Updated statistics based on selected filters")
        print("\n⏹️  Press Ctrl+C to stop")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8005/brazil_delivery_revenue_dashboard.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()