#
# Example file for working with os.path module
#
import os
from os import path
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item exists: ", path.exists("sampleFile.txt"))
print("Item is a file: ", path.isfile("sampleFile.txt"))
print("Item is a dir: ", path.isdir("sampleFile.txt"))

# Work with file paths
print("Item's full path is ", path.realpath("sampleFile.txt"))
print("Item's path and name is ", path.split(path.realpath("sampleFile.txt")))
itemTuple = path.split(path.realpath("sampleFile.txt"))
print("File name is ", itemTuple[1])
print("File dir is ", itemTuple[0])

# Get the modification time
mtime = time.ctime(path.getmtime("sampleFile.txt"))
print("Local modified time is: ", mtime)
print("Datetime  modified time is: ", datetime.fromtimestamp(path.getmtime("sampleFile.txt")))

# Calculate how long ago the item was modified
timeDelta = datetime.now() - datetime.fromtimestamp(path.getmtime("sampleFile.txt"))
print(f"It has been {timeDelta} since the file was modified")
print(f"Or, {timeDelta.total_seconds()} seconds")
