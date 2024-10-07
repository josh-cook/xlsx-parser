#!/bin/bash

echo "Installing pandas..."
pip3 install --user pandas --break-system-packages

echo "Installing pyperclip..."
pip3 install --user pyperclip --break-system-packages

echo "Installing openpyxl..."
pip3 install --user openpyxl --break-system-packages

echo "All packages have been installed!"