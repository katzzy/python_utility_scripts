# This script modifies line endings of all files in a folder and its subfolders to CRLF (Windows style)
# to avoid git warnings when comitting files with LF (Linux style) line endings
import os


def check_string_contains(string, string_list):
    for s in string_list:
        if s in string:
            return True
    return False


def is_binary(file_name):
    try:
        with open(file_name, "tr") as check_file:  # try open file in text mode
            check_file.read()
            return False
    except:  # if fail then file is non-text (binary)
        return True


def modify_line_endings(folder_path, ignore_folders=[]):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(s in root for s in ignore_folders):
                continue
            file_path = os.path.join(root, file)
            if is_binary(file_path):
                continue
            with open(file_path, "r", newline="", encoding="utf-8") as f:
                content = f.readlines()
            # len(content) == 1 for some one line files with no line endings, you should handle this case manually
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
