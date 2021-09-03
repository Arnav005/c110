import os
import shutil
source=input("enter a source folder name")
print(source)
destination=input("enter the destination folder name")
print(destination)
source=source+'/'
destination=destination+'/'
list_of_files=os.listdir(source)
for files in list_of_files:
    shutil.move((source+files),destination)
