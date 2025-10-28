import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    # Dictionary of file type categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.java', '.cpp']
    }

    # Create folders if not present
    for folder in file_types.keys():
        new_folder = os.path.join(folder_path, folder)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

    # Move files to their respective folders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, file_name))
                    print(f"📁 Moved: {file_name} → {folder}")
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, file_name))
                print(f"📦 Moved: {file_name} → Others")

    print("\n✅ File organization complete!")

# Example usage:
folder = input("Enter the path of the folder to organize: ")
organize_files(folder)
