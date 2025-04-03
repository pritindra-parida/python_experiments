# Saving All Tables to 1 json file


import pandas as pd
from bs4 import BeautifulSoup
import json

# Path to the saved HTML file
file_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/member_details.html"

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all tables in the HTML file
tables = soup.find_all('table')

# Initialize a dictionary to store all table data
all_tables = {}

# Process each table
for table_index, table in enumerate(tables, start=1):
    # Extract rows from the table
    rows = table.find_all('tr')
    
    # Extract headers
    headers = [th.text.strip() for th in rows[0].find_all('th')] if rows else []  # Extract headers if present
    table_data = []

    # Extract table rows
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if headers and len(cells) == len(headers):  # Match headers to data
            row_data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
            table_data.append(row_data)
        else:  # For headerless or mismatched tables
            row_data = [cell.text.strip() for cell in cells]
            table_data.append(row_data)

    # Add the table to the dictionary
    table_name = f"table_{table_index}"
    all_tables[table_name] = table_data

# Save all tables to a single JSON file
output_file = "all_tables.json"
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(all_tables, json_file, indent=4, ensure_ascii=False)
print(f"All tables have been saved to {output_file}")
