"""
PDF Utilities for Validation Strategist Agent
Handles PDF document reading operations
"""

import os
from .document_processor import check_and_install_package

def read_pdf_pypdf2(file_path):
    """
    Read PDF content using PyPDF2 library.
    
    Args:
        file_path (str): Path to the PDF file
    
    Returns:
        str: Text content of the PDF
    """
    if not check_and_install_package('PyPDF2'):
        return "Error: PyPDF2 library not available"
    
    try:
        import PyPDF2
        
        if not os.path.exists(file_path):
            return f"Error: File not found: {file_path}"
        
        content = []
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                content.append(page.extract_text())
        
        return '\n'.join(content)
    
    except Exception as e:
        return f"Error reading PDF file with PyPDF2: {str(e)}"

def read_pdf_pdfplumber(file_path):
    """
    Read PDF content using pdfplumber library (better text extraction).
    
    Args:
        file_path (str): Path to the PDF file
    
    Returns:
        str: Text content of the PDF
    """
    if not check_and_install_package('pdfplumber'):
        return "Error: pdfplumber library not available"
    
    try:
        import pdfplumber
        
        if not os.path.exists(file_path):
            return f"Error: File not found: {file_path}"
        
        content = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    content.append(text)
        
        return '\n'.join(content)
    
    except Exception as e:
        return f"Error reading PDF file with pdfplumber: {str(e)}"

def read_pdf(file_path, prefer_pdfplumber=True):
    """
    Read PDF content using the best available library.
    
    Args:
        file_path (str): Path to the PDF file
        prefer_pdfplumber (bool): Try pdfplumber first (better extraction)
    
    Returns:
        str: Text content of the PDF
    """
    if prefer_pdfplumber:
        # Try pdfplumber first (better text extraction)
        content = read_pdf_pdfplumber(file_path)
        if not content.startswith("Error:"):
            return content
        
        # Fallback to PyPDF2
        print("🔄 Falling back to PyPDF2...")
        return read_pdf_pypdf2(file_path)
    else:
        # Try PyPDF2 first
        content = read_pdf_pypdf2(file_path)
        if not content.startswith("Error:"):
            return content
        
        # Fallback to pdfplumber
        print("🔄 Falling back to pdfplumber...")
        return read_pdf_pdfplumber(file_path)

def extract_pdf_metadata(file_path):
    """
    Extract metadata from PDF file.
    
    Args:
        file_path (str): Path to the PDF file
    
    Returns:
        dict: PDF metadata
    """
    if not check_and_install_package('PyPDF2'):
        return {"error": "PyPDF2 library not available"}
    
    try:
        import PyPDF2
        
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}
        
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            metadata = pdf_reader.metadata
            
            return {
                'title': metadata.get('/Title', 'Unknown'),
                'author': metadata.get('/Author', 'Unknown'),
                'subject': metadata.get('/Subject', 'Unknown'),
                'creator': metadata.get('/Creator', 'Unknown'),
                'producer': metadata.get('/Producer', 'Unknown'),
                'creation_date': metadata.get('/CreationDate', 'Unknown'),
                'modification_date': metadata.get('/ModDate', 'Unknown'),
                'page_count': len(pdf_reader.pages)
            }
    
    except Exception as e:
        return {"error": f"Error extracting PDF metadata: {str(e)}"}

def analyze_architecture_pdf(file_path):
    """
    Analyze a PDF architecture document for key information.
    
    Args:
        file_path (str): Path to the architecture PDF
    
    Returns:
        dict: Analysis results with key sections and insights
    """
    content = read_pdf(file_path)
    
    if content.startswith("Error:"):
        return {"error": content}
    
    # Extract metadata
    metadata = extract_pdf_metadata(file_path)
    
    # Basic analysis
    analysis = {
        "file_path": file_path,
        "metadata": metadata,
        "content_length": len(content),
        "word_count": len(content.split()),
        "sections": [],
        "key_terms": [],
        "summary": ""
    }
    
    # Look for common architecture document sections
    section_keywords = [
        "overview", "architecture", "interface", "component", "module",
        "design", "specification", "requirements", "implementation",
        "integration", "system", "subsystem", "protocol", "api"
    ]
    
    lines = content.split('\n')
    current_section = None
    
    for line in lines:
        line_lower = line.lower().strip()
        
        # Look for section headers
        for keyword in section_keywords:
            if keyword in line_lower and (line_lower.startswith(keyword) or 
                                        any(c in line for c in ['1.', '2.', '3.', '#'])):
                if line.strip() not in analysis["sections"]:
                    analysis["sections"].append(line.strip())
                current_section = line.strip()
                break
    
    # Extract key terms (simple approach)
    key_terms = set()
    for keyword in section_keywords:
        if keyword in content.lower():
            key_terms.add(keyword)
    
    analysis["key_terms"] = list(key_terms)
    
    # Create simple summary
    first_lines = lines[:10]
    analysis["summary"] = ' '.join(first_lines)[:500] + "..." if len(' '.join(first_lines)) > 500 else ' '.join(first_lines)
    
    return analysis

if __name__ == "__main__":
    # Test PDF utilities
    print("🧪 Testing PDF utilities...")
    
    # This would test with an actual PDF file
    test_file = "test_architecture.pdf"
    
    if os.path.exists(test_file):
        print(f"📖 Testing PDF reading with: {test_file}")
        
        # Test reading
        content = read_pdf(test_file)
        if not content.startswith("Error:"):
            print(f"✅ PDF reading successful! Content length: {len(content)}")
            
            # Test metadata extraction
            metadata = extract_pdf_metadata(test_file)
            if "error" not in metadata:
                print(f"✅ Metadata extraction successful! Pages: {metadata['page_count']}")
            else:
                print(f"❌ Metadata extraction failed: {metadata['error']}")
            
            # Test analysis
            analysis = analyze_architecture_pdf(test_file)
            if "error" not in analysis:
                print(f"✅ PDF analysis successful! Sections found: {len(analysis['sections'])}")
            else:
                print(f"❌ PDF analysis failed: {analysis['error']}")
        else:
            print(f"❌ PDF reading failed: {content}")
    else:
        print("ℹ️  No test PDF file found. Create 'test_architecture.pdf' to test PDF utilities.")