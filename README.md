# XLSX Parser for Discounted Vehicles

This repository contains a basic Python XLSX parser designed to process data for discounted vehicles. The output can be copied to your clipboard for easy access.


## Installation

### Clone Repo
```bash
git clone git@github.com:josh-cook/xlsx-parser.git
cd xlsx-parser
```

### Install Required Packages: 

Run the `install_packages.sh` script to create a virtual environment and install the required packages:
```bash
bash install_packages.sh
```

## Usage
After installing the required packages, ensure that you update the file path in the csvReader.py script to point to your specific XLSX file.

Activate your virtual environment: 

```bash
source venv/bin/activate
```

To run the parser, use the following command in your terminal:

```bash
python3 csvReader.py path/to/file
```

Deactivate your virtual environment:

```bash
deactivate
```

<br>

### Notes
Ensure that you have Python 3 and pip installed on your system.