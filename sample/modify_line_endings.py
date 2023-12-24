# This script modifies line endings of all files in a folder
# and its subfolders to CRLF (Windows style)
# to avoid git warnings when comitting files with LF (Linux style) line endings
import os


# Not recommended to use try-except for implementing logic,
# but in this case, it will handle all possible exceptions,
# which works more reliably and will make the script more robust.
# If you don't want to use try-except, you can use the following code instead:
# from binaryornot.check import is_binary  # pip install binaryornot
def is_binary(file_name):
    try:
        with open(file_name, "tr") as check_file:  # try open file in text mode
            check_file.read()
            return False
    except UnicodeDecodeError:
        return True


def modify_line_endings(folder_path, ignore_folders=None):
    if ignore_folders is None:
        ignore_folders = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(s in root for s in ignore_folders):
                continue
            file_path = os.path.join(root, file)
            if is_binary(file_path):
                continue
            with open(file_path, "r", newline="", encoding="utf-8") as f:
                content = f.readlines()
            # len(content) == 1 for some one line files with no line endings,
            # you should handle this case manually
            if content is None or len(content) == 0 or len(content) == 1:
                continue
            if "\r\n" in content[0]:
                continue
            with open(file_path, "w", newline="\r\n", encoding="utf-8") as f:
                f.writelines(content)
            print("Line endings modified for file: {}".format(file_path))

    print("Line endings modified successfully.")


# Example usage
folder_path = r"your_folder_path"
modify_line_endings(folder_path, [".git", "node_modules"])
