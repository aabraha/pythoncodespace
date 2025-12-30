#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("sampleFile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("sampleFile.txt")
        
    # # let's make a backup copy path by appending "bak" to the src name
    dst = src + ".bak"

    # # now use the shell to make a copy of the file
    shutil.copy(src, dst) # it only copy the content and not the metadata
    #shutil.copy2(src, dst) # conpy the content and metadata


    # # rename the original file
    os.rename("sampleFile.txt", "renamedSampleFile.txt")
    
# switch working file into the renamed file
if path.exists("renamedSampleFile.txt"):
    # now put things into a ZIP archive
    srcPath = path.realpath("renamedSampleFile.txt")
    rootDir, tail = path.split(srcPath)
    shutil.make_archive("archive", "zip", rootDir)

if path.exists("renamedSampleFile.txt") and path.exists("sampleFile.txt.bak"):
    # more fine-grained control over ZIP files
      with ZipFile("testZip.zip", "w") as newZip:
           newZip.write("renamedSampleFile.txt")
           newZip.write("sampleFile.txt.bak")