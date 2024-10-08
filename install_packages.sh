#!/bin/bash

# Create a venv if one does not exist
if [ ! -d "venv" ]; then
  echo "Creating Virtual Environment"
  python3 -m venv venv
fi

source venv/bin/activate

# Install required packages within the virtual environment
echo "Installing pandas..."
pip install pandas

echo "Installing pyperclip..."
pip install pyperclip

echo "Installing openpyxl..."
pip install openpyxl

echo "All packages have been installed in the virtual environment!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To deactivate, run: deactivate"
