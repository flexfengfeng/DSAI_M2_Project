#!/usr/bin/env python3
"""
Test with maximum visibility settings
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
    
    with socketserver.TCPServer(("", 8012), Handler) as httpd:
        print("👁️ Maximum Visibility Test at http://localhost:8012")
        print("🐛 Debug: http://localhost:8012/debug_revenue_map.html")
        print("📊 Dashboard: http://localhost:8012/brazil_delivery_revenue_dashboard.html")
        print("\n🔧 Applied fixes:")
        print("   • Full opacity (1.0)")
        print("   • Fixed size (20px)")
        print("   • Black borders (3px width)")
        print("   • Purple fill (#6A1B9A)")
        print("\n🔍 Symbols should now be clearly visible!")
        
        threading.Timer(1, lambda: webbrowser.open('http://localhost:8012/debug_revenue_map.html')).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Server stopped")

if __name__ == "__main__":
    start_server()