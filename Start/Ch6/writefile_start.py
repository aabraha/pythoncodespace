# write files using the built-in Python file methods
# No need to import any lib
#


# Open a file for writing and create it if it doesn't exist
sampleFile = open("sampleFile.txt","w+")
sampleFile.write("This is sample text in sample file.\n")
sampleFile.close()


# Open the file for appending text to the end
sampleFile = open("sampleFile.txt","a+")

# write some lines of data to the file
sampleFile.write("This is more sample text appended in sample file.\r")
sampleFile.write("This is even more sample text appended in sample file.")

# close the file when done
sampleFile.close()