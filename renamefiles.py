# code to create and rename files in a folder

# import modules
from pathlib import Path

# Access Desktop to create folder
home = Path.home()

Desktop = home / "Desktop"

# create folder if it doesn't exist
folder = Desktop / "files"

folder.mkdir(exist_ok = True)

# create txt files
if len(list(folder.glob('*.txt'))) <= 5:
 for i in range(1,6):
    filename = f"old_{i:02}_file.txt"
    file_path = folder/filename
    file_path.touch()
    print (f"file created: {filename}")

# make it interactive
choice = input("\n Do you want to rename the txt files? (y/n) ").strip()
prefix = input("\n choose prefix to name it (eg prefix_01_.txt)")

#change name of files if choice = y
if choice == 'y':
    if folder.exists():
        print('\n renaming ......')
        for i, file in enumerate(folder.glob('*.txt'), start = 1):
            new_filename = f"{prefix}_{i:02}_.txt"
            new_path = folder / new_filename
            file.rename(new_path)
            print(f"\Renamed {file.name} -> {new_filename}")
    else:
        print("\n Parent Folder does not exist")
else:
   print ("\n No renaming — exiting.")

#delete txt files
delete_choice = input("\n Delete txt files? (y/n)")

if delete_choice == "y":
   print("\n deleted")
   for txt_file in folder.glob("*.txt"):
      txt_file.unlink()
    
else:
   print("No deleting -- skipping")