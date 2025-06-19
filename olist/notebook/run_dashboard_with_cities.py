#!/usr/bin/env python3
"""
Run the dashboard with city selector
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
    
    with socketserver.TCPServer(("", 8003), Handler) as httpd:
        print("🚀 Dashboard with Cities running at http://localhost:8003")
        print("📊 URL: http://localhost:8003/brazil_delivery_dashboard_with_cities.html")
        print("\n✨ New Features:")
        print("   • City selector with 1,647 cities")
        print("   • Filter by states, cities, categories, and order count")
        print("   • Real-time filtering and statistics")
        print("\n⏹️  Press Ctrl+C to stop")
        
        # Auto-open the dashboard
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8003/brazil_delivery_dashboard_with_cities.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()