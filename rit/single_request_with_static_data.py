import os
import requests

url = "https://httpbin.org/post"
post_data = {
    "pass": "",
    "mem_family_code": "0012345678000",
    "mem_code": "",
    "csrf_token": "aa0980a8sdf809aw34ph1io2h34",
    "fc_submit": "Submit"
}

try:
    response = requests.post(url, data=post_data)
    response.raise_for_status()  # Raise an exception for HTTP error codes
    
    # Define the local path where you want to save the file
    save_path = r"C:\Users\pritparida\Downloads\Documents\My Data\Liku\result.htm"
    
    # Save the complete response content (webpage) to the specified .htm file
    with open(save_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"The webpage has been successfully saved as {save_path}.")

except requests.RequestException as e:
    print(f"An error occurred: {e}")
