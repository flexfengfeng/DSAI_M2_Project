#!/usr/bin/env python3
"""
Start Brazil Delivery Time Analysis Dashboard (English Version)
Simplified startup script
"""

import os
import webbrowser
import http.server
import socketserver
import threading
import time

def start_dashboard(port=8000):
    """Start the dashboard"""
    # Switch to notebook directory
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(notebook_dir)
    
    print("🚀 Starting Brazil Delivery Time Analysis Dashboard...")
    print(f"📁 Working directory: {notebook_dir}")
    
    try:
        # Create HTTP server
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        
        print(f"✅ HTTP server started successfully")
        print(f"🌐 Access URL: http://localhost:{port}/brazil_delivery_dashboard_en.html")
        
        # Start server in new thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        
        # Wait for server to start
        time.sleep(2)
        
        # Auto-open browser
        url = f"http://localhost:{port}/brazil_delivery_dashboard_en.html"
        try:
            webbrowser.open(url)
            print("🎯 Browser opened automatically")
        except:
            print("⚠️  Please manually open browser and visit the URL above")
        
        print("\n" + "="*60)
        print("📊 Dashboard is now running!")
        print("="*60)
        print("Features:")
        print("• Left panel: Filters and data summary")
        print("• Top right: Interactive map")
        print("• Bottom right: Three analysis charts")
        print("="*60)
        print("💡 Press Ctrl+C to stop the server")
        print("="*60)
        
        # Keep server running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Stopping server...")
            httpd.shutdown()
            print("✅ Server stopped")
            
    except Exception as e:
        print(f"❌ Failed to start: {e}")

if __name__ == "__main__":
    start_dashboard()