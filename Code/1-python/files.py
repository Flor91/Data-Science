import os
import shutil

my_files = ["accounts.txt", "details.csv", "invite.docx"]

for filename in my_files:
    print(os.path.join("Users", "asweigart", filename))

cwd = os.getcwd()
print(os.getcwd())

os.chdir(os.path.join(os.getcwd(), "1-python"))

print(os.getcwd())

os.chdir(cwd)

# os.mkdir('test-dir')

print("\nos.path.isabs('/')")
print(os.path.isabs("/"))

print("\nos.path.isabs('..')")
print(os.path.isabs(".."))

print("\nos.path.exists('setup.py')")
print(os.path.exists("setup.py"))

print("\nos.path.isdir('/')")
print(os.path.isdir("/"))

print("\nos.path.getsize(os.getcwd())")
print(os.path.getsize(cwd))

print("\nos.path.listdir(cwd)")
print(os.listdir(cwd))

# shutil.copy(os.path.join(os.getcwd(), '.gitignore'), os.path.join(os.getcwd(), '1-python'))

# shutil.copytree(os.path.join(os.getcwd(), '1-python'), os.path.join(os.getcwd(), '1-python', 'test_dir'))

# shutil.move(os.path.join(os.getcwd(), '1-python', 'test_dir'), os.path.join(os.getcwd(), '1-python', 'test-dir'))
"""
Calling os.unlink(path) or Path.unlink() will delete the file at path.

Calling os.rmdir(path) or Path.rmdir() will delete the folder at path. This folder must be empty of any files or folders.

Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
"""

# os.unlink(os.path.join(os.getcwd(), '1-python', '.gitignore'))
# shutil.rmtree(os.path.join(os.getcwd(), '1-python', 'test-dir'))

for folder_name, subfolders, filenames in os.walk(
        os.path.join(os.getcwd(), "1-python")):
    print("The current folder is {}".format(folder_name))
    for subfolder in subfolders:
        print("SUBFOLDER OF {}: {}".format(folder_name, subfolder))
    for filename in filenames:
        print("FILE INSIDE {}: {}".format(folder_name, filename))
    print("")
