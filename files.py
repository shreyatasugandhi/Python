import sys
import os
import random

# open or create a new file with write permission
test_file = open("test_file.txt", "w")
print("File mode is : ", test_file.mode)
print("File name is: ", test_file.name)

# write to the file
test_file.write("Write me to the file\n")

# close the file
test_file.close()

# read from a file
test_file = open("test_file.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()

# delete the file
os.remove("test_file.txt")