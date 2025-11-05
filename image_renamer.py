# import os
# from pathlib import Path

# def rename_images(folder_path):
#     """
#     Renames all .jpg images in a folder to IMG01, IMG02, etc.
    
#     Args:
#         folder_path: Path to the folder containing images
#     """
#     # Line 1: Import os module for file operations
#     # Line 2: Import Path from pathlib for modern path handling
    
#     # Check if folder exists
#     # os.path.exists() returns True if the path exists, False otherwise
#     if not os.path.exists(folder_path):
#         print(f"Error: Folder '{folder_path}' does not exist!")
#         return
    
#     # Get all .jpg files in the folder
#     # os.listdir() returns a list of all files and folders in the directory
#     # We filter only files ending with .jpg (case-insensitive)
#     jpg_files = [f for f in os.listdir(folder_path) 
#                  if f.lower().endswith(".jpg") and os.path.isfile(os.path.join(folder_path, f))]
    
#     # Check if there are any images
#     if not jpg_files:
#         print("No .jpg images found in the folder!")
#         return
    
#     # Sort files alphabetically for consistent ordering
#     # sorted() arranges files in alphabetical order
#     jpg_files.sort()
    
#     print(f"Found {len(jpg_files)} images. Starting rename process...\n")
    
#     # Counter for renamed images
#     renamed_count = 0
    
#     # Loop through each image file with enumeration
#     # enumerate() gives us both the index (starting from 1) and the filename
#     for index, old_name in enumerate(jpg_files, start=1):
#         # Create new filename with zero-padded number
#         # f-string formats the number with leading zeros (e.g., 01, 02, 03)
#         # :02d means: format as decimal, minimum 2 digits, pad with zeros
#         new_name = f"IMG{index:02d}.jpg"
        
#         # Build full paths for old and new filenames
#         # os.path.join() safely combines folder path and filename
#         old_path = os.path.join(folder_path, old_name)
#         new_path = os.path.join(folder_path, new_name)
        
#         # Skip if the file already has the correct name
#         if old_name == new_name:
#             print(f"Skipped: '{old_name}' (already correctly named)")
#             continue
        
#         # Check if new filename already exists to avoid overwriting
#         if os.path.exists(new_path):
#             print(f"Warning: '{new_name}' already exists. Skipping '{old_name}'")
#             continue
        
#         try:
#             # Rename the file
#             # os.rename() changes the file name from old_path to new_path
#             os.rename(old_path, new_path)
#             print(f"Renamed: '{old_name}' → '{new_name}'")
#             renamed_count += 1
            
#         except Exception as e:
#             # Catch any errors during renaming (permissions, file in use, etc.)
#             print(f"Error renaming '{old_name}': {e}")
    
#     # Print summary
#     print(f"\n✓ Rename complete! {renamed_count} images renamed successfully.")


# # Main execution block
# if __name__ == "__main__":
#     # Get the desktop path
#     # Path.home() returns the user's home directory (C:\Users\YourName on Windows)
#     # We then join it with 'Desktop' to get the desktop path
#     desktop_path = os.path.join(Path.home(), 'Desktop')
    
#     # Specify your folder name
#     folder_name = "ImageRenamer"
    
#     # Build full folder path
#     folder_path = os.path.join(desktop_path, folder_name)
    
#     print(f"Target folder: {folder_path}\n")
    
#     # Call the rename function



# import os
# IMGS_PATH = "C:\\Users\\DELL\\Desktop\\ImageRenamer"
# IMAGES = os.listdir(IMGS_PATH)

# TRACK = 0

# for index in IMAGES:
#     os.rename(os.path.join(IMGS_PATH, index), os.path.join(IMGS_PATH, f"IMG{TRACK + 1}.jpg"))
#     TRACK += 1
# print("Done Renaming Images..")