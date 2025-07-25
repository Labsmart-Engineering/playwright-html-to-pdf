#!/bin/bash

echo "🚀 Setting up Playwright HTML to PDF Converter..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

echo "✅ Python dependencies installed successfully"

# Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
python3 -m playwright install chromium

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Playwright browsers"
    exit 1
fi

echo "✅ Playwright browsers installed successfully"

# Make the script executable
chmod +x html_to_pdf.py

# Test the installation
echo "🧪 Testing the installation..."
python3 html_to_pdf.py sample.html -o test_output.pdf

if [ $? -eq 0 ] && [ -f "test_output.pdf" ]; then
    echo "✅ Installation test successful!"
    echo "📄 Test PDF generated: test_output.pdf"
    rm test_output.pdf  # Clean up test file
else
    echo "❌ Installation test failed"
    exit 1
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "Usage examples:"
echo "  python3 html_to_pdf.py sample.html"
echo "  python3 html_to_pdf.py myfile.html -o output.pdf"
echo "  python3 html_to_pdf.py document.html --format Letter --landscape"
echo ""
echo "For more options, run: python3 html_to_pdf.py --help"