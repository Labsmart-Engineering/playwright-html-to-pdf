# 📝 HTML to PDF Converter - Command Reference

Quick reference guide for converting HTML files to PDF using Playwright.

## 🚀 Basic Usage

### Convert HTML to PDF (same name)
```bash
python3 html_to_pdf.py sample.html
```
**Output:** `sample.pdf`

### Specify custom output file
```bash
python3 html_to_pdf.py sample.html -o my_document.pdf
```
**Output:** `my_document.pdf`

---

## 📄 Page Format Options

### Standard Formats
```bash
python3 html_to_pdf.py sample.html --format A4      # Default
python3 html_to_pdf.py sample.html --format A3      # Larger
python3 html_to_pdf.py sample.html --format Letter  # US Standard
python3 html_to_pdf.py sample.html --format Legal   # US Legal
python3 html_to_pdf.py sample.html --format Tabloid # Large format
```

**Available formats:** A0, A1, A2, A3, A4, A5, A6, Letter, Legal, Tabloid, Ledger

---

## 🔄 Orientation Options

### Portrait (Default)
```bash
python3 html_to_pdf.py sample.html
```

### Landscape
```bash
python3 html_to_pdf.py sample.html --landscape
```

### Landscape with custom output
```bash
python3 html_to_pdf.py sample.html --landscape -o wide_report.pdf
```

---

## 📏 Margin Settings

### Default margins (1cm all sides)
```bash
python3 html_to_pdf.py sample.html
```

### Custom margins
```bash
# Individual margins
python3 html_to_pdf.py sample.html --margin-top 2cm --margin-bottom 2cm

# All margins
python3 html_to_pdf.py sample.html --margin-top 1.5cm --margin-right 1.5cm --margin-bottom 1.5cm --margin-left 1.5cm

# No margins
python3 html_to_pdf.py sample.html --margin-top 0 --margin-right 0 --margin-bottom 0 --margin-left 0
```

**Margin units:** `cm`, `mm`, `in`, `px`

---

## 🎨 Styling Options

### Include backgrounds (Default)
```bash
python3 html_to_pdf.py sample.html
```

### Disable backgrounds
```bash
python3 html_to_pdf.py sample.html --no-background
```

---

## 💡 Common Use Cases

### 1. Standard Document
```bash
python3 html_to_pdf.py report.html
```

### 2. Professional Report
```bash
python3 html_to_pdf.py report.html -o final_report.pdf --format Letter --margin-top 2cm --margin-bottom 2cm
```

### 3. Wide Chart/Table
```bash
python3 html_to_pdf.py chart.html --landscape --format A3 -o wide_chart.pdf
```

### 4. Print-ready Document
```bash
python3 html_to_pdf.py document.html --no-background --margin-top 2.5cm --margin-bottom 2.5cm
```

### 5. Presentation Slides
```bash
python3 html_to_pdf.py slides.html --landscape --format Tabloid -o presentation.pdf
```

### 6. Invoice/Receipt
```bash
python3 html_to_pdf.py invoice.html -o invoice_001.pdf --format Letter
```

---

## 🔧 Advanced Examples

### Minimal margins for web pages
```bash
python3 html_to_pdf.py webpage.html --margin-top 0.5cm --margin-right 0.5cm --margin-bottom 0.5cm --margin-left 0.5cm
```

### Large format poster
```bash
python3 html_to_pdf.py poster.html --format A1 --landscape -o poster.pdf
```

### Multiple files batch conversion
```bash
# Convert multiple files
python3 html_to_pdf.py page1.html -o chapter1.pdf
python3 html_to_pdf.py page2.html -o chapter2.pdf
python3 html_to_pdf.py page3.html -o chapter3.pdf
```

---

## ❓ Help & Options

### Show all available options
```bash
python3 html_to_pdf.py --help
```

### Check if setup is working
```bash
python3 html_to_pdf.py sample.html -o test.pdf
```

---

## 📂 File Paths

### Relative paths
```bash
python3 html_to_pdf.py ./documents/report.html
python3 html_to_pdf.py ../templates/invoice.html -o ./output/invoice.pdf
```

### Absolute paths
```bash
python3 html_to_pdf.py /Users/username/Documents/file.html -o /Users/username/Desktop/output.pdf
```

---

## ⚡ Quick Reference Table

| Option | Description | Example |
|--------|-------------|---------|
| `html_file` | Input HTML file (required) | `sample.html` |
| `-o, --output` | Output PDF path | `-o report.pdf` |
| `--format` | Page format | `--format Letter` |
| `--landscape` | Landscape orientation | `--landscape` |
| `--no-background` | Disable backgrounds | `--no-background` |
| `--margin-top` | Top margin | `--margin-top 2cm` |
| `--margin-right` | Right margin | `--margin-right 1.5cm` |
| `--margin-bottom` | Bottom margin | `--margin-bottom 2cm` |
| `--margin-left` | Left margin | `--margin-left 1.5cm` |

---

## 🎯 Success Tips

1. **Always test first:** Use `sample.html` to verify setup
2. **Check file paths:** Ensure HTML file exists
3. **Use quotes for spaces:** `"my file.html"` for files with spaces
4. **Preview in browser:** Check HTML rendering before conversion
5. **Monitor output:** Look for success message ✅

---

## 🚨 Troubleshooting

### Command not found
Make sure you're in the project directory:
```bash
cd /Users/sachin/Documents/GitHub/playwright-html-to-pdf
```

### File not found
Check the HTML file path:
```bash
ls -la sample.html  # Verify file exists
```

### Permission denied
Make script executable:
```bash
chmod +x html_to_pdf.py
```

---

**🎉 Happy PDF generating!**