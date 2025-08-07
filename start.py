#!/usr/bin/env python3
"""
Startup script for AI Search Chatbot
Checks dependencies and starts the Flask application
"""

import sys
import subprocess
import os

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'flask',
        'flask_cors',
        'requests',
        'bs4',
        'python-dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} (missing)")
    
    return missing_packages

def install_dependencies():
    """Install missing dependencies"""
    print("\n🔧 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def start_app():
    """Start the Flask application"""
    print("\n🚀 Starting AI Search Chatbot...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server\n")
    
    # Import and run the Flask app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

def main():
    """Main startup function"""
    print("🤖 AI Search Chatbot - Startup Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Make sure you're in the project directory.")
        sys.exit(1)
    
    # Check dependencies
    print("\n📦 Checking dependencies...")
    missing = check_dependencies()
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        install_deps = input("Would you like to install them now? (y/n): ").lower().strip()
        
        if install_deps == 'y':
            if not install_dependencies():
                print("❌ Failed to install dependencies. Please install manually:")
                print("   pip install -r requirements.txt")
                sys.exit(1)
        else:
            print("❌ Cannot start without required dependencies")
            sys.exit(1)
    
    print("\n✅ All dependencies are satisfied!")
    
    # Start the application
    try:
        start_app()
    except KeyboardInterrupt:
        print("\n\n👋 Chatbot stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()