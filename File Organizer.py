# File Organizer (CLI)

import os
import shutil

print("File Organizer")

# Ask user for folder path
path = input("Enter folder path to organize: ")

# Check if path exists
if not os.path.exists(path):
    print("Invalid path!")
else:
    # File type categories
    image_ext = ['.jpg', '.jpeg', '.png', '.gif']
    doc_ext = ['.pdf', '.docx', '.txt']
    video_ext = ['.mp4', '.mkv', '.avi']

    # Folder names
    image_folder = os.path.join(path, "Images")
    doc_folder = os.path.join(path, "Documents")
    video_folder = os.path.join(path, "Videos")

    # Create folders if not exist
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(doc_folder, exist_ok=True)
    os.makedirs(video_folder, exist_ok=True)

    # Go through all files
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file)

        # Move files based on type
        if ext.lower() in image_ext:
            shutil.move(file_path, os.path.join(image_folder, file))

        elif ext.lower() in doc_ext:
            shutil.move(file_path, os.path.join(doc_folder, file))

        elif ext.lower() in video_ext:
            shutil.move(file_path, os.path.join(video_folder, file))

    print("Files organized successfully!")