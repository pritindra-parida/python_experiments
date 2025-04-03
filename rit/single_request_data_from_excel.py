import os
import pandas as pd
import requests

# Define the file path to your CSV file containing the POST data
# csv_file_path = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\data.csv"

# If you want to use an Excel file instead, uncomment the next line and comment out the CSV section:
excel_file_path = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\data.xlsx"

try:
    # Read data from CSV file
    # df = pd.read_csv(csv_file_path)
    
    # Uncomment the following lines if using an Excel file:
    df = pd.read_excel(excel_file_path)
    
    # Validate that the necessary columns exist
    expected_columns = {'pass', 'mem_family_code', 'mem_code', 'csrf_token', 'fc_submit'}
    if not expected_columns.issubset(df.columns):
        raise Exception(f"The input file must contain the following columns: {expected_columns}")
    
    # Extract the values from the first row
    post_data = {
        'pass': df.loc[0, 'pass'],
        'mem_family_code': df.loc[0, 'mem_family_code'],
        'mem_code': df.loc[0, 'mem_code'],
        'csrf_token': df.loc[0, 'csrf_token'],
        'fc_submit': df.loc[0, 'fc_submit'],
    }
    
    # Define the target URL for testing the POST request
    url = "https://httpbin.org/post"
    
    # Execute the POST request with the extracted data
    response = requests.post(url, data=post_data)
    response.raise_for_status()  # Raises an exception for HTTP error codes.
    
    # Define the path where the response will be saved locally.
    
    
    ############# File extension should be **** .mht ****  ##############
    ## File name should contain current time stamp ##
    
    result_file_path = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\result_temp.htm"
    with open(result_file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"POST request successful. Response saved to {result_file_path}.")
    print(f"Data sent: {post_data}")

except Exception as e:
    print(f"An error occurred: {e}")
    
