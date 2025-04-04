# Code Generated by Sidekick is for learning and experimentation purposes only.
import os
import shutil

def copy_and_rename(source_file, destination_folder, base_number, copies, increment):
    """
    Copies the source_file 'copies' times into destination_folder.
    Each copied file is renamed with an incremental number based on base_number and increment.

    Parameters:
    - source_file: Full path to the file to be copied.
    - destination_folder: Folder where the copied files will be placed.
    - base_number: Starting number (e.g., 293381000 for filename 000293381000.html).
    - copies: Number of copies to create.
    - increment: Value to add to the base number for each subsequent copy.
    """
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    for i in range(copies):
        # Calculate the new number by adding the increment multiplied by the copy index
        new_number = base_number + (i * increment)
        # Format the new filename with zero padding to a total of 12 digits and add the .html extension
        new_filename = f"{new_number:012d}.html"
        new_filepath = os.path.join(destination_folder, new_filename)
        
        # Copy the file, preserving metadata
        shutil.copy2(source_file, new_filepath)
        print(f"Created copy: {new_filepath}")

# Specific paths and settings
source_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets/member_details.html"
destination_path = "C:/Users/pritparida/Downloads/Documents/My Data/Liku/assets"
base_number = 293381000   # Starting number for file naming (adjust if needed)
copies = 10               # Number of copies to be generated
increment = 1000          # Incremental increase for each file's name

copy_and_rename(source_path, destination_path, base_number, copies, increment)
