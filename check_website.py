#!/usr/bin/env python3
"""
Check Website Files and Configuration
This script verifies that all necessary website files are present and properly configured.
"""

import os
import sys
import re
from pathlib import Path

def check_website_files():
    """Check if all required website files are present and configured correctly."""
    
    # Define the base directory
    website_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Checking website files in: {website_dir}")
    
    # List of required files
    required_files = [
        "index.html",
        "pdf_viewer.html",
        "css/style.css",
        "js/main.js",
        "server.py"
    ]
    
    # Check each required file
    missing_files = []
    for file_path in required_files:
        full_path = os.path.join(website_dir, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
            print(f"❌ Missing file: {file_path}")
        else:
            print(f"✅ Found file: {file_path}")
    
    if missing_files:
        print(f"\nWarning: {len(missing_files)} required files are missing.")
    else:
        print("\nAll required files are present.")
    
    # Check PDF references in index.html
    index_path = os.path.join(website_dir, "index.html")
    if os.path.exists(index_path):
        print("\nChecking PDF references in index.html...")
        with open(index_path, 'r') as f:
            content = f.read()
        
        # Find all PDF references
        pdf_refs = re.findall(r'data-pdf="([^"]+)"', content)
        
        # Output directory should be one level up from website
        output_dir = os.path.join(os.path.dirname(website_dir), "output")
        
        if not os.path.exists(output_dir):
            print(f"❌ Output directory not found: {output_dir}")
        else:
            print(f"✅ Output directory found: {output_dir}")
            
            # Check each referenced PDF
            missing_pdfs = []
            for pdf_ref in pdf_refs:
                # Convert relative path to absolute
                if pdf_ref.startswith("../output/"):
                    pdf_path = os.path.join(os.path.dirname(website_dir), pdf_ref[3:])
                else:
                    pdf_path = os.path.join(website_dir, pdf_ref)
                
                if not os.path.exists(pdf_path):
                    missing_pdfs.append(pdf_ref)
                    print(f"❌ Referenced PDF not found: {pdf_ref}")
            
            if missing_pdfs:
                print(f"\nWarning: {len(missing_pdfs)} referenced PDFs are missing.")
            else:
                print("\nAll referenced PDFs are available.")
    
    # Check JavaScript functionality
    js_path = os.path.join(website_dir, "js", "main.js")
    if os.path.exists(js_path):
        print("\nChecking JavaScript functionality...")
        with open(js_path, 'r') as f:
            js_content = f.read()
        
        # Check for key functions
        if "setupPdfViewer" in js_content:
            print("✅ PDF viewer setup function found")
        else:
            print("❌ PDF viewer setup function missing")
        
        # Check for PDF link handling
        if "data-pdf" in js_content:
            print("✅ PDF link attribute handling found")
        else:
            print("❌ PDF link attribute handling missing")
    
    # Overall assessment
    print("\n--- Website Check Summary ---")
    if not missing_files and os.path.exists(output_dir) and not missing_pdfs:
        print("✅ Website files appear to be correctly configured.")
        print("✅ Run 'python server.py' to start the website locally.")
    else:
        print("❌ Website configuration has issues that need to be addressed.")
        if missing_files:
            print(f"   - Missing {len(missing_files)} required files")
        if not os.path.exists(output_dir):
            print("   - Output directory not found")
        if 'missing_pdfs' in locals() and missing_pdfs:
            print(f"   - Missing {len(missing_pdfs)} referenced PDFs")

if __name__ == "__main__":
    check_website_files() 