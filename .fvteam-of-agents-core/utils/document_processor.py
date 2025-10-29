"""
Document Processing Utilities for Validation Strategist Agent
Handles .docx, .pdf, and .md file operations with automatic library management
"""

import os
import sys
import subprocess
import importlib.util

def check_and_install_package(package_name, import_name=None):
    """
    Check if a package is installed, and if not, ask user permission to install it.
    
    Args:
        package_name (str): Name of the package to install (pip package name)
        import_name (str): Name to use for import (if different from package_name)
    
    Returns:
        bool: True if package is available, False otherwise
    """
    if import_name is None:
        import_name = package_name
    
    # Check if package is already installed
    spec = importlib.util.find_spec(import_name)
    if spec is not None:
        print(f"✅ {package_name} is already installed.")
        return True
    
    # Ask user permission to install
    print(f"📦 {package_name} is required for document processing.")
    user_response = input(f"Do you want to install {package_name}? (y/n): ").lower().strip()
    
    if user_response in ['y', 'yes']:
        try:
            print(f"🔄 Installing {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✅ {package_name} installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package_name}: {e}")
            return False
    else:
        print(f"❌ {package_name} installation declined. Document processing may be limited.")
        return False

def ensure_document_libraries():
    """
    Ensure all required document processing libraries are available.
    
    Returns:
        dict: Status of each library (True/False)
    """
    print("🔍 Checking document processing libraries...")
    
    libraries = {
        'python-docx': check_and_install_package('python-docx', 'docx'),
        'PyPDF2': check_and_install_package('PyPDF2'),
        'pdfplumber': check_and_install_package('pdfplumber')
    }
    
    return libraries

def get_feature_filename(base_name, feature_name, extension='md'):
    """
    Generate filename with feature name and timestamp.
    
    Args:
        base_name (str): Base name (e.g., 'validation_strategy')
        feature_name (str): Feature name to include
        extension (str): File extension without dot
    
    Returns:
        str: Generated filename
    """
    from datetime import datetime
    
    # Clean feature name for filename
    clean_feature = feature_name.replace(' ', '_').replace('/', '_').replace('\\', '_')
    timestamp = datetime.now().strftime('%Y%m%d')
    
    return f"{base_name}_{clean_feature}_{timestamp}.{extension}"

def ensure_output_directory(output_path):
    """
    Ensure output directory exists, create if necessary.
    
    Args:
        output_path (str): Path to output directory
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"📁 Created output directory: {output_path}")

if __name__ == "__main__":
    # Test library availability
    print("🧪 Testing document processing setup...")
    libraries = ensure_document_libraries()
    
    print("\n📊 Library Status:")
    for lib, status in libraries.items():
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {lib}: {'Available' if status else 'Not available'}")
    
    if all(libraries.values()):
        print("\n🎉 All document processing libraries are ready!")
    else:
        print("\n⚠️  Some libraries are missing. Document processing may be limited.")