import pandas as pd
import pyperclip
import sys

# Path is read from first argument passed in
file_path = sys.argv[1]

try:
    # Read xlsx file and skip the headers
    excel_file = pd.read_excel(file_path, skiprows=1)
except Exception as e:
    print(f"Error reading the file: {e}")
    sys.exit(1)

output_list = []

for index, row in excel_file.iterrows():
    # Access the actual column names and values for each row
    column_b_name = excel_file.columns[1]
    column_h_name = excel_file.columns[7]
    value_b = row[column_b_name]
    value_h = row[column_h_name]
    
    # output for each row
    output = f"discountedVehicles.set(\"{value_b}\", {value_h})"
    output_list.append(output)
    
# Combine the outputs and copy to clipboard
combined_output = "\n".join(output_list)
pyperclip.copy(combined_output)

print("Successfully copied to clipboard")