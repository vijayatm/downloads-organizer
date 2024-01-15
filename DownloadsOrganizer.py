import os
import shutil
import subprocess

def organize_download_folder(download_folder):
    # Create category folders
    category_folders = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'ico'],
        'Videos': ['mp4', 'mov', 'm4v', 'avi', 'mkv'],
        'HTML': ['html', 'htm'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'rtf', 'pages'],
        'Music': ['mp3', 'wav', 'flac', 'aac'],
        'Applications': ['dmg', 'app', 'pkg'],
        'Compressed': ['zip', 'rar', 'tar', 'gz'],
        # Add more categories and their corresponding file extensions as needed
    }

    # Create category folders if they don't exist
    for category, extensions in category_folders.items():
        category_path = os.path.join(download_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Create 'Others' category folder
    others_folder = os.path.join(download_folder, 'Others')
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)

    # List all files in the download folder
    files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]

    # Counters for moved files
    moved_files_count = 0
    ignored_files_count = 0

    # Organize files based on their extensions
    for file in files:
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()[1:]  # Convert to lowercase and remove the dot

        # Determine the category based on the file extension
        file_category = None
        for category, extensions in category_folders.items():
            if file_extension in extensions:
                file_category = category
                break

        # If the file extension is not in any specified category, move it to 'Others' category
        if not file_category:
            file_category = 'Others'

        # Move the file to its corresponding category folder
        src_path = os.path.join(download_folder, file)
        dest_path = os.path.join(download_folder, file_category, file)

        # Check if the item is a file before moving
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
            moved_files_count += 1
            print(f"Moved: {file} to {file_category} folder")
        else:
            ignored_files_count += 1
            print(f"Ignored: {file} (Not a file)")

    # Display a notification with statistics
    show_notification(f"Organizing complete\nMoved Files: {moved_files_count}\nIgnored Files: {ignored_files_count}")

def show_notification(message):
    try:
        subprocess.run([
            'osascript',
            '-e', f'display notification "{message}" with title "File Organizer"'
        ])
    except Exception as e:
        print(f"Error displaying notification: {e}")

if __name__ == "__main__":
    # Replace 'path/to/download/folder' with the actual path to your download folder
    download_folder_path = '/Users/vijay-7431/Downloads'

    if os.path.exists(download_folder_path):
        organize_download_folder(download_folder_path)
    else:
        print(f"The specified download folder '{download_folder_path}' does not exist.")
