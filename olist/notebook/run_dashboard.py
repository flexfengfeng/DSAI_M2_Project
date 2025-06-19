#!/usr/bin/env python3
"""
运行巴西送货时间仪表盘
1. 生成数据文件
2. 启动本地HTTP服务器
3. 自动打开浏览器
"""

import os
import sys
import webbrowser
import http.server
import socketserver
import threading
import time
from dashboard_data_generator import DeliveryDashboardDataGenerator

def generate_data():
    """生成仪表盘数据"""
    print("正在生成仪表盘数据...")
    try:
        generator = DeliveryDashboardDataGenerator()
        data_file = generator.generate_dashboard_data()
        print(f"✅ 数据生成成功: {data_file}")
        return True
    except Exception as e:
        print(f"❌ 数据生成失败: {e}")
        print("将使用示例数据运行仪表盘")
        return False

def start_server(port=8000):
    """启动HTTP服务器"""
    try:
        # 切换到notebook目录
        notebook_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(notebook_dir)
        
        # 创建HTTP服务器
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        
        print(f"🚀 HTTP服务器启动成功")
        print(f"📍 服务地址: http://localhost:{port}")
        print(f"📁 服务目录: {notebook_dir}")
        
        # 在新线程中启动服务器
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        
        return httpd, port
    except Exception as e:
        print(f"❌ 服务器启动失败: {e}")
        return None, None

def open_browser(port):
    """打开浏览器"""
    url = f"http://localhost:{port}/delivery_dashboard_enhanced.html"
    print(f"🌐 正在打开浏览器: {url}")
    
    # 等待服务器启动
    time.sleep(2)
    
    try:
        webbrowser.open(url)
        print("✅ 浏览器已打开")
    except Exception as e:
        print(f"❌ 无法自动打开浏览器: {e}")
        print(f"请手动访问: {url}")

def main():
    """主函数"""
    print("=" * 60)
    print("🎯 巴西送货时间分析仪表盘")
    print("=" * 60)
    
    # 1. 生成数据
    data_generated = generate_data()
    
    # 2. 启动服务器
    httpd, port = start_server()
    if not httpd:
        print("❌ 无法启动服务器，程序退出")
        sys.exit(1)
    
    # 3. 打开浏览器
    open_browser(port)
    
    print("\n" + "=" * 60)
    print("📊 仪表盘功能说明:")
    print("• 左侧面板: 数据筛选和统计摘要")
    print("• 右上方: 交互式地图显示各地区送货时间")
    print("• 右下方: 三个分析图表")
    print("  - 各州平均送货天数柱状图")
    print("  - 送货时间分类饼图")
    print("  - 送货天数分布直方图")
    print("=" * 60)
    print("💡 使用提示:")
    print("• 点击地图上的点查看详细信息")
    print("• 使用左侧筛选器过滤数据")
    print("• 拖动滑块调整最小订单数")
    print("• 点击'刷新数据'按钮更新数据")
    print("=" * 60)
    
    try:
        print("\n⌨️  按 Ctrl+C 停止服务器")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 正在停止服务器...")
        httpd.shutdown()
        print("✅ 服务器已停止")

if __name__ == "__main__":
    main()