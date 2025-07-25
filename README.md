# Playwright HTML to PDF Converter

A simple Python tool to convert HTML files to PDF using Playwright. This tool provides high-fidelity PDF generation that preserves CSS styling, fonts, and layout.

## Features

- 🎯 High-quality PDF generation with accurate rendering
- 🎨 Preserves CSS styling, fonts, and layouts
- ⚙️ Customizable PDF options (format, margins, orientation)
- 🚀 Fast conversion with async processing
- 📱 Responsive design support
- 🔧 Command-line interface for easy automation

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## Usage

### Basic Usage

Convert an HTML file to PDF:
```bash
python html_to_pdf.py sample.html
```

This will create `sample.pdf` in the same directory.

### Advanced Usage

Specify output file:
```bash
python html_to_pdf.py sample.html -o my_document.pdf
```

Custom page format and margins:
```bash
python html_to_pdf.py sample.html --format Letter --margin-top 2cm --margin-bottom 2cm
```

Landscape orientation without background:
```bash
python html_to_pdf.py sample.html --landscape --no-background
```

### Command Line Options

- `html_file`: Path to the HTML file to convert (required)
- `-o, --output`: Output PDF file path (optional)
- `--format`: Page format - A4, A3, A2, A1, A0, Letter, Legal, Tabloid, Ledger (default: A4)
- `--landscape`: Use landscape orientation
- `--no-background`: Disable background printing
- `--margin-top`: Top margin (default: 1cm)
- `--margin-right`: Right margin (default: 1cm)  
- `--margin-bottom`: Bottom margin (default: 1cm)
- `--margin-left`: Left margin (default: 1cm)

### Examples

```bash
# Basic conversion
python html_to_pdf.py report.html

# Custom output location
python html_to_pdf.py report.html -o /path/to/output/report.pdf

# Letter format with larger margins
python html_to_pdf.py document.html --format Letter --margin-top 2.5cm --margin-bottom 2.5cm

# Landscape orientation for wide content
python html_to_pdf.py chart.html --landscape -o landscape_chart.pdf
```

## Sample Files

- `sample.html`: A sample HTML file with various styling elements to test the conversion
- `html_to_pdf.py`: The main conversion script
- `requirements.txt`: Python dependencies

## How It Works

The tool uses Playwright's Chromium browser to:

1. Load the HTML file in a headless browser
2. Wait for all content and resources to load
3. Generate a PDF with the specified options
4. Save the PDF to the specified location

This approach ensures that the PDF output matches exactly what you would see in a browser, including:
- CSS styling and layouts
- Web fonts
- Background images and colors
- Responsive design elements
- JavaScript-generated content (after page load)

## Troubleshooting

### Browser Installation Issues
If you encounter browser installation issues:
```bash
playwright install --force chromium
```

### Permission Issues
Make sure you have write permissions to the output directory:
```bash
chmod +w /path/to/output/directory
```

### Large HTML Files
For large HTML files with many resources, the tool automatically waits for the page to finish loading before generating the PDF.

## Requirements

- Python 3.7+
- Playwright
- Chromium browser (installed automatically with Playwright)

## License

This project is open source and available under the MIT License.