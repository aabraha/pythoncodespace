#
# Read and write files using the built-in Python file methods
#

    
# Open the file and read the contents
openFile = open("sampleFile.txt", "r")
# if openFile.mode == 'r':
#     # use the read() function to read the entire file
#     content = openFile.read()
#     print(content)

# read line by line
if openFile.mode == 'r':
    lines = openFile.readlines()
    for line in lines:
        print(line)

#close
openFile.close()