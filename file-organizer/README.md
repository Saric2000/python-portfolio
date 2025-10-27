# File Organizer Automation

Automates the organization of files in a folder by their file type.  
Sorts files into subfolders based on their extensions (e.g., `.pdf`, `.jpg`, `.mp4`) and moves them automatically.  

---

## Features
- Automatically detects all files in the specified folder
- Creates subfolders for each file type
- Moves files into the corresponding folder
- Easy to customize for any folder on your computer

---

## Tech Stack
- Python 3.x
- Standard libraries: `os`, `shutil`

---

## How to Use
1. Clone or download this repository.
2. Open `main.py` and set the `source_folder` variable to the folder you want to organize:
   ```python
   source_folder = r"C:\Users\Admin\Downloads" 


Before running the script:
Downloads/
├─ report.pdf
├─ photo.jpg
├─ video.mp4
├─ notes.txt

After running the script:
Downloads/
├─ PDF_files/
│  └─ report.pdf
├─ JPG_files/
│  └─ photo.jpg
├─ MP4_files/
│  └─ video.mp4
├─ TXT_files/
│  └─ notes.txt
``