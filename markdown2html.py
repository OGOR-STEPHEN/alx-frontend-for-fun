#!/usr/bin/python3
"""
This script converts a Markdown file to an HTML file.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Requirements:
    - The input must be a valid Markdown file
    - The output will be an HTML file
"""

import sys
import os
import markdown

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get the input and output filenames from arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the markdown file exists
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    # Read the content of the markdown file
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()

        # Convert markdown to HTML using the markdown library
        html_content = markdown.markdown(markdown_content)

        # Write the converted content to the output HTML file
        with open(html_file, 'w') as html_out:
            html_out.write(html_content)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
