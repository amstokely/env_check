import sys
import os

def check_file_exists(file_path):
    if os.path.isfile(file_path):
        print(f"File {file_path} exists.")
        return True
    else:
        print(f"File {file_path} does not exist.")
        return False

if __name__ == "__main__":
    file_path = sys.argv[1]
    check_file_exists(file_path)
