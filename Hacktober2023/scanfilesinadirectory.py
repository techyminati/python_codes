import os

def scan_files(directory):
    files_list = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            files_list.append(os.path.join(foldername, filename))
    return files_list

if __name__ == "__main__":
    # Replace 'directory_path' with the path of the directory you want to scan
    directory_path = input("Enter the directory path to scan: ")

    if os.path.isdir(directory_path):
        files = scan_files(directory_path)
        if files:
            print("List of files in the directory:")
            for file_path in files:
                print(file_path)
        else:
            print("No files found in the directory.")
    else:
        print("Invalid directory path. Please provide a valid directory path.")
