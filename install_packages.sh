#!/bin/bash

# Create a venv if one does not exist
if [ ! -d "venv" ]; then
  echo "Creating Virtual Environment"
  python3 -m venv venv
fi

source venv/bin/activate

# Install required packages within the virtual environment
echo "Installing required packages..."
pip install -r requirements.txt

echo "All packages have been installed in the virtual environment!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To deactivate, run: deactivate"
