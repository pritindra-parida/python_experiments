### Only Printing Data ###

from bs4 import BeautifulSoup

# Path to the saved HTML file
file_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/member_details.html"

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

tables = soup.find_all('table')

# Iterate over each table
for table_index, table in enumerate(tables, start=1):
    print(f"Table {table_index}:")
    
    # Extract table rows
    rows = table.find_all('tr')
    
    for row in rows:
        # Extract cells from the row
        cells = row.find_all(['th', 'td'])  # 'th' for headers, 'td' for data cells
        cell_values = [cell.text.strip() for cell in cells]  # Get the text content
        print("\t".join(cell_values))  # Print the row as a tab-separated line
    
    print("\n") 
