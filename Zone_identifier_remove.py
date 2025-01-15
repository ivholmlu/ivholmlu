# Clean identifier files automatically generated when unpacking files or moving files in WSL2.

import os

def delete_zone_identifier_files():
    """
    Iterate through the current directory and delete all files ending with .Zone.Identifier.
    """
    current_directory = os.getcwd()  # Get the current working directory
    for root, _, files in os.walk(current_directory):
        for file in files:
            if file.endswith("Zone.Identifier"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    delete_zone_identifier_files()
