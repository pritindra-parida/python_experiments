import os
import time
import pandas as pd
import requests

# Define the file path to your Excel file containing the POST data
excel_file_path = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\assets\var_data.xlsx"

# Define the directory where the results will be saved
results_directory = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\results"
os.makedirs(results_directory, exist_ok=True)

try:
    # Read data from the Excel file (default is the first sheet)
    df = pd.read_excel(excel_file_path)
    
    # Replace any missing values (NaN) with empty strings
    df.fillna("", inplace=True)
    
    # Validate that the necessary columns exist in the Excel file
    expected_columns = {'var1', 'var2', 'var3', 'var4', 'var5'}
    if not expected_columns.issubset(df.columns):
        raise Exception(f"The input file must contain the following columns: {expected_columns}")
    
    # Limit processing to the first 10 rows or the total number of rows if fewer than 10
    num_rows = min(len(df), 10)
    
    # Define the target URL for testing the POST request
    url = "https://httpbin.org/post"
    
    # Loop through each row, send POST request, and save the response with a filename based on var2
    for i in range(num_rows):
        # Extract values for the current row
        post_data = {
            'var1': df.loc[i, 'var1'],
            'var2': df.loc[i, 'var2'],
            'var3': df.loc[i, 'var3'],
            'var4': df.loc[i, 'var4'],
            'var5': df.loc[i, 'var5']
        }
        
        # Send the POST request with the extracted data
        response = requests.post(url, data=post_data)
        response.raise_for_status()  # Raises an exception if an HTTP error occurs
        
        # Sanitize var2 to create a valid filename (optional, here we simply strip whitespace)
        file_name = str(df.loc[i, 'var2']).strip() + ".htm"
        result_file_path = os.path.join(results_directory, file_name)
        
        with open(result_file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        
        print(f"POST request for row {i+1} successful. Response saved to {result_file_path}.")
        
        # Wait for 10 seconds before sending the next request
        time.sleep(10)
    
except Exception as e:
    print(f"An error occurred: {e}")
