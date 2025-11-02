"""
Generic DOCX to TXT Converter
Converts any DOCX file to a plain text file.

Usage:
    python docx_to_txt.py <input_file.docx> [output_file.txt]
    
If output_file is not specified, it will use the same name as input with .txt extension.
"""

import sys
import os
from pathlib import Path

try:
    import docx
except ImportError:
    print("Error: python-docx library is not installed.")
    print("Please install it using: pip install python-docx")
    sys.exit(1)


def extract_text_from_docx(file_path):
    """
    Extract all text from a DOCX file.
    
    Args:
        file_path (str): Path to the input DOCX file
        
    Returns:
        str: Extracted text content
    """
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading DOCX file: {e}")
        sys.exit(1)


def convert_docx_to_txt(input_file, output_file=None):
    """
    Convert a DOCX file to TXT format.
    
    Args:
        input_file (str): Path to the input DOCX file
        output_file (str, optional): Path to the output TXT file
    """
    # Validate input file
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    if not input_file.lower().endswith('.docx'):
        print("Warning: Input file does not have .docx extension.")
    
    # Determine output file path
    if output_file is None:
        output_file = Path(input_file).with_suffix('.txt')
    
    # Extract text from DOCX
    print(f"Reading from: {input_file}")
    text = extract_text_from_docx(input_file)
    
    # Save to TXT file
    try:
        with open(output_file, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        print(f"Conversion complete! Text saved to: {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python docx_to_txt.py <input_file.docx> [output_file.txt]")
        print("\nExample:")
        print("  python docx_to_txt.py document.docx")
        print("  python docx_to_txt.py document.docx output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_docx_to_txt(input_file, output_file)


if __name__ == "__main__":
    main()
