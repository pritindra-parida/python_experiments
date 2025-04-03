import os
import json
import pandas as pd  # retained import if needed in future modifications
from bs4 import BeautifulSoup

# Define the input and output directories
assets_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/assets_fc"
output_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/results/assets_fc"
os.makedirs(output_path, exist_ok=True)  # Create the output directory if it doesn't exist

# Loop through all HTML files in the assets directory
for filename in os.listdir(assets_path):
    if filename.lower().endswith(".html"):
        file_path = os.path.join(assets_path, filename)
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find all tables in the HTML file
        tables = soup.find_all('table')

        # Process the second table (index 1) if it exists
        if len(tables) < 2:
            print(f"File {filename} does not contain at least 2 tables, skipping.")
            continue

        table = tables[1]

        # Extract rows from the table
        rows = table.find_all('tr')

        # Extract headers and rows from the table
        headers = [th.text.strip() for th in rows[0].find_all('th')] if rows else []
        table_data = []

        for row in rows[1:]:  # Skip the header row
            cells = row.find_all('td')
            if headers and len(cells) == len(headers):  # Match headers to data
                row_data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
                table_data.append(row_data)
            else:  # No headers or mismatched cells
                row_data = [cell.text.strip() for cell in cells]
                table_data.append(row_data)

        # Define the JSON file name based on the input file name
        base_name = os.path.splitext(filename)[0]
        json_file_name = os.path.join(output_path, f"{base_name}.json")

        # Save the extracted table data to a JSON file
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(table_data, json_file, indent=4, ensure_ascii=False)

        print(f"Second table from '{filename}' saved to '{json_file_name}'")
