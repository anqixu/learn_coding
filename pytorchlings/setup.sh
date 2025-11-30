#!/bin/bash
# Setup script for PyTorchlings

set -e

echo "🔥 PyTorchlings Setup 🔥"
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $python_version"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "✗ pip3 not found. Please install pip first."
    exit 1
fi
echo "✓ pip3 is available"

# Create virtual environment (optional)
read -p "Create a virtual environment? (recommended) [y/N]: " create_venv
if [[ $create_venv == "y" || $create_venv == "Y" ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ Virtual environment created and activated"
fi

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "✓ Dependencies installed"

# Make pytorchlings executable
chmod +x pytorchlings
echo "✓ Made pytorchlings executable"

# Run a quick test
echo ""
echo "Running quick test..."
if python3 -c "import torch; print(f'PyTorch {torch.__version__} installed successfully!')"; then
    echo "✓ PyTorch is working!"
else
    echo "✗ PyTorch test failed"
    exit 1
fi

echo ""
echo "🎉 Setup complete! 🎉"
echo ""
echo "Get started with:"
echo "  ./pytorchlings           # Start in watch mode"
echo "  ./pytorchlings list      # See all exercises"
echo "  ./pytorchlings --help    # Show help"
echo ""
echo "Happy learning! 🚀"
