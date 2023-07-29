import os

folder_path = "C:/Users/User/OneDrive/Desktop/PO Folders"

def deleting_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf") and int(file_name[-6: -4]) % 2 != 0:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            print(f"Deleted file: {file_name}")

deleting_files(folder_path)
