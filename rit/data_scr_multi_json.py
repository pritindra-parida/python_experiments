import pandas as pd
from bs4 import BeautifulSoup
import json

# Path to the saved HTML file
file_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/fc_member_list.html"

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all tables in the HTML file
tables = soup.find_all('table')

# Initialize a list to store all table data
all_tables_data = []

# Process each table
for table_index, table in enumerate(tables, start=1):
    # Extract rows from the table
    rows = table.find_all('tr')
    
    # Extract headers and rows
    headers = [th.text.strip() for th in rows[0].find_all('th')] if rows else []  # Extract headers if present
    table_data = []

    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if headers and len(cells) == len(headers):  # Match headers to data
            row_data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
            table_data.append(row_data)
        else:  # No headers or mismatched cells
            row_data = [cell.text.strip() for cell in cells]
            table_data.append(row_data)

    # Save table to a JSON file
    json_file_name = f"table_{table_index}.json"
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(table_data, json_file, indent=4, ensure_ascii=False)
    print(f"Table {table_index} saved to {json_file_name}")

    # Add the table data to the combined list
    # all_tables_data.append(table_data)

# Save all tables to a single JSON file
# combined_json_file_name = "all_tables.json"
# with open(combined_json_file_name, 'w', encoding='utf-8') as combined_json_file:
#    json.dump(all_tables_data, combined_json_file, indent=4, ensure_ascii=False)
# print(f"All tables combined and saved to {combined_json_file_name}")
