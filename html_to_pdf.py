#!/usr/bin/env python3
"""
HTML to PDF Converter using Playwright
"""

import asyncio
import argparse
import sys
from pathlib import Path
from playwright.async_api import async_playwright


async def html_to_pdf(html_file: str, output_file: str = None, **pdf_options):
    """
    Convert an HTML file to PDF using Playwright
    
    Args:
        html_file (str): Path to the HTML file to convert
        output_file (str, optional): Output PDF file path. If None, uses HTML filename with .pdf extension
        **pdf_options: Additional PDF generation options
    """
    
    html_path = Path(html_file).resolve()
    
    if not html_path.exists():
        print(f"Error: HTML file '{html_file}' not found.")
        sys.exit(1)
    
    if output_file is None:
        output_file = html_path.with_suffix('.pdf')
    else:
        output_file = Path(output_file).resolve()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Load the HTML file
        await page.goto(f"file://{html_path}")
        
        # Wait for any dynamic content to load
        await page.wait_for_load_state('networkidle')
        
        # Generate PDF with default options
        default_options = {
            'format': 'A4',
            'print_background': True,
            'margin': {
                'top': '1cm',
                'right': '1cm',
                'bottom': '1cm',
                'left': '1cm'
            }
        }
        
        # Merge user options with defaults
        pdf_options = {**default_options, **pdf_options}
        
        # Generate PDF
        await page.pdf(path=str(output_file), **pdf_options)
        
        await browser.close()
    
    print(f"✅ PDF generated successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert HTML files to PDF using Playwright')
    parser.add_argument('html_file', help='Path to the HTML file to convert')
    parser.add_argument('-o', '--output', help='Output PDF file path (optional)')
    parser.add_argument('--format', default='A4', help='Page format (default: A4)')
    parser.add_argument('--no-background', action='store_true', help='Disable background printing')
    parser.add_argument('--landscape', action='store_true', help='Use landscape orientation')
    parser.add_argument('--margin-top', default='1cm', help='Top margin (default: 1cm)')
    parser.add_argument('--margin-right', default='1cm', help='Right margin (default: 1cm)')
    parser.add_argument('--margin-bottom', default='1cm', help='Bottom margin (default: 1cm)')
    parser.add_argument('--margin-left', default='1cm', help='Left margin (default: 1cm)')
    
    args = parser.parse_args()
    
    # Build PDF options from arguments
    pdf_options = {
        'format': args.format,
        'print_background': not args.no_background,
        'landscape': args.landscape,
        'margin': {
            'top': args.margin_top,
            'right': args.margin_right,
            'bottom': args.margin_bottom,
            'left': args.margin_left
        }
    }
    
    # Run the conversion
    asyncio.run(html_to_pdf(args.html_file, args.output, **pdf_options))


if __name__ == '__main__':
    main()