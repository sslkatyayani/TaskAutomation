import os

# Step 1: Specify the folder containing the files
folder_path = "rename_folder"  # Make sure this folder exists in the same directory as your script

# Step 2: Loop through all files in the folder
for count, filename in enumerate(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, filename)

    # Step 3: Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Step 4: Extract file extension
    ext = filename.split('.')[-1] if '.' in filename else ''

    # Step 5: Create new name with same extension
    new_name = f"file_{count + 1}.{ext}" if ext else f"file_{count + 1}"

    # Step 6: Build full path for old and new filenames
    new_file_path = os.path.join(folder_path, new_name)

    # Step 7: Rename the file
    os.rename(file_path, new_file_path)
    print(f"Renamed: {filename} -> {new_name}")