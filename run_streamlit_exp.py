#!/usr/bin/env python3
"""
启动脚本：运行实验版本的 Streamlit 应用
支持三种 persona 选择的 Safety ChatBot System
"""

import subprocess
import sys
import os

def main():
    """启动 Streamlit 实验应用"""
    try:
        # 检查是否安装了 streamlit
        import streamlit
        print("✅ Streamlit 已安装")
    except ImportError:
        print("❌ Streamlit 未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit 安装完成")
    
    # 启动应用
    print("🚀 启动 Safety ChatBot System - Experimental")
    print("📝 功能特性:")
    print("   - 三种 persona 选择：严格教官、友好同事、AI助手")
    print("   - 基于实验版本的聊天机器人")
    print("   - 支持对话导出")
    print("   - 实时 API Key 管理")
    print("\n🌐 应用将在浏览器中打开...")
    
    # 运行 streamlit 应用
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", 
        "streamlit_exp_app.py",
        "--server.port", "8501",
        "--server.address", "localhost"
    ])

if __name__ == "__main__":
    main()
