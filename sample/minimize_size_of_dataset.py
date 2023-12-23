# This script deletes a specified percentage of files from each folder in a directory
# to minimize the size of the dataset for testing purposes
import os
import random


def delete_files(directory_path, percentage_to_delete):
    # Iterate over each folder in the directory
    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)
        if os.path.isdir(folder_path):
            # Get a list of all files in the folder
            files = os.listdir(folder_path)
            # Calculate the number of files to delete
            num_files_to_delete = int(len(files) * percentage_to_delete)
            # Shuffle the list of files
            random.shuffle(files)
            # Delete the specified number of files
            for file_name in files[:num_files_to_delete]:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")


# Example usage
directory_path = r"your_directory_path"
percentage_to_delete = 0.5
delete_files(directory_path, percentage_to_delete)