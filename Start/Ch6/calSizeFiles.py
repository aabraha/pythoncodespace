# Count the size in bytes of text files in a directory

# There is a set of files in the "learning-python-3980343" directory, which is at the same directory level that your code is running in. There are no subdirectories within this "learning-python-3980343" folder.

# Your task: Calculate and return the total size in bytes of the text files within the directory. Only include text files that end with ".txt" in your calculation. Other files should be ignored.

# Parameters

# No parameters are passed to your function.

# Result

# int: Total byte count of all the text files in the directory
import os
from os import path

def file_info():
    # Your code goes here.
    # 
    totalSize = 0
    # Get the absolute path of the current script file
    script_path = os.path.abspath(__file__) 
    # Get the directory name from the script path
    script_dir = os.path.dirname(script_path)
    print(f"\nPath: {script_path}, \nDir: {script_dir}")
    
    with os.scandir(script_dir + "/deps") as entries:
        for entry in entries:
            if(entry.name.endswith(".txt") and path.isfile(entry)):
                totalSize += path.getsize(entry)

    return totalSize

print("Total size(bytes): ", file_info())