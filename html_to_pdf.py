#!/usr/bin/env python3
"""
HTML to PDF Converter using Playwright
"""

import asyncio
import argparse
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
        raise FileNotFoundError(f"HTML file '{html_file}' not found.")
    
    if output_file is None:
        output_file = html_path.with_suffix('.pdf')
    else:
        output_file = Path(output_file).resolve()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto(f"file://{html_path}")
        await page.wait_for_load_state('networkidle')
        
        default_options = {
            'format': 'A4',
            'print_background': True,
            'margin': {
                'top': '0',
                'right': '0',
                'bottom': '0',
                'left': '0'
            }
        }
        
        pdf_options = {**default_options, **pdf_options}
        await page.pdf(path=str(output_file), **pdf_options)
        await browser.close()
    
    print(f"✅ PDF generated successfully: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert HTML files to PDF using Playwright')
    parser.add_argument('html_file', help='Path to the HTML file to convert')
    parser.add_argument('-o', '--output', help='Output PDF file path (optional)')
    
    args = parser.parse_args()
    
    asyncio.run(html_to_pdf(args.html_file, args.output))


if __name__ == '__main__':
    main()