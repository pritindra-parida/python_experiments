import pandas as pd
from bs4 import BeautifulSoup
import json
import os

# Path to the saved HTML file
file_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/member_details.html"

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all tables in the HTML file
tables = soup.find_all('table')

# Since there are exactly 2 tables, process the second table (index 1)
table = tables[1]

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

# Define the path to save the JSON file
save_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/results"
os.makedirs(save_path, exist_ok=True)  # Create the directory if it doesn't exist
json_file_name = os.path.join(save_path, "table_2.json")

# Save the second table to a JSON file
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(table_data, json_file, indent=4, ensure_ascii=False)
print(f"Second table saved to {json_file_name}")


