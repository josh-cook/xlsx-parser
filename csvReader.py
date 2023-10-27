import pandas as pd
import pyperclip

# Replace path
file_path = 'path/to/file'

# Read xlsx file and skip the headers
df = pd.read_excel(file_path, skiprows=1)

output_list = []

for index, row in df.iterrows():
    # Access the actual column names and values for each row
    column_b_name = df.columns[1]
    column_h_name = df.columns[7]
    value_b = row[column_b_name]
    value_h = row[column_h_name]
    
    # output for each row
    output = f"discountedVehicles.set(\"{value_b}\", {value_h})"
    output_list.append(output)
    
# Combine the outputs and copy to clipboard
combined_output = "\n".join(output_list)
pyperclip.copy(combined_output)

print("Successfully copied to clipboard")