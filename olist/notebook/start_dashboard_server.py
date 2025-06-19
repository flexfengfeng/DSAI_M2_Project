#!/usr/bin/env python3
"""
Simple HTTP server to serve the dashboard with proper CORS handling
"""
import http.server
import socketserver
import webbrowser
import os
import sys

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def start_server(port=8000):
    """Start HTTP server for dashboard"""
    # Change to notebook directory
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(notebook_dir)
    
    # Check if required files exist
    if not os.path.exists('dashboard_data.json'):
        print("❌ dashboard_data.json not found!")
        print("Run: python dashboard_data_generator_en.py")
        return
    
    if not os.path.exists('brazil_delivery_dashboard_en.html'):
        print("❌ brazil_delivery_dashboard_en.html not found!")
        return
    
    try:
        with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
            print(f"🚀 Dashboard server starting on port {port}")
            print(f"📊 Dashboard URL: http://localhost:{port}/brazil_delivery_dashboard_en.html")
            print("🔄 Press Ctrl+C to stop the server")
            
            # Auto-open browser
            webbrowser.open(f'http://localhost:{port}/brazil_delivery_dashboard_en.html')
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"python start_dashboard_server.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    start_server(port)