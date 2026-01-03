# Wap in python to print he contents of a directory using the OS module.Search online for the function which does that.

import os

# specify the directory path you want to list
path = "/"

# get list of all files and directories
contents = os.listdir(path)

# print each item
print("Contents of the directory:", path)
for item in contents:
    print(item)
