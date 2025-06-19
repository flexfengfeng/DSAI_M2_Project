#!/usr/bin/env python3
"""
启动巴西送货时间分析仪表盘
简化版启动脚本
"""

import os
import webbrowser
import http.server
import socketserver
import threading
import time

def start_dashboard(port=8000):
    """启动仪表盘"""
    # 切换到notebook目录
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(notebook_dir)
    
    print("🚀 启动巴西送货时间分析仪表盘...")
    print(f"📁 工作目录: {notebook_dir}")
    
    try:
        # 创建HTTP服务器
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        
        print(f"✅ HTTP服务器启动成功")
        print(f"🌐 访问地址: http://localhost:{port}/integrated_delivery_dashboard.html")
        
        # 在新线程中启动服务器
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        
        # 等待服务器启动
        time.sleep(2)
        
        # 自动打开浏览器
        url = f"http://localhost:{port}/integrated_delivery_dashboard.html"
        try:
            webbrowser.open(url)
            print("🎯 浏览器已自动打开")
        except:
            print("⚠️  请手动打开浏览器访问上述地址")
        
        print("\n" + "="*60)
        print("📊 仪表盘已启动！")
        print("="*60)
        print("功能说明:")
        print("• 左侧: 筛选器和数据摘要")
        print("• 右上: 交互式地图")
        print("• 右下: 三个分析图表")
        print("="*60)
        print("💡 按 Ctrl+C 停止服务器")
        print("="*60)
        
        # 保持服务器运行
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 正在停止服务器...")
            httpd.shutdown()
            print("✅ 服务器已停止")
            
    except Exception as e:
        print(f"❌ 启动失败: {e}")

if __name__ == "__main__":
    start_dashboard()