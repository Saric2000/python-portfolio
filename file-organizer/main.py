import os
import shutil


source_folder = r"C:\Users\Admin\Downloads"  #Change to your own folder

files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

for file in files:
    ext = file.split(".")[-1]
    folder_path = os.path.join(source_folder, ext.upper() + "_files")
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(source_folder, file), os.path.join(folder_path, file))

print("Files organized successfully!")
