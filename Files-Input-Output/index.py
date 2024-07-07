
"""
Modes :
1. r
2. w
3. x
4. a
5. b
6. t
7. +
"""

# r+ : read + overwrite , ptr(start) , no truncate

# w+ : read + overwrite , ptr(start) ,truncate

# a+ : read + append , ptr(end) , no truncate


f = open(r"C:\Users\KIIT\Desktop\Personal-Stuffs\Python\Files-Input-Output\file.txt","r")
data = f.read()
print(data)
print(type(data))

# f.readline() to read one line at a time

f.close()

#! if file not exist and we open in w or a mode then python automatically create one for us


# other way to open file : below is code -> in this way we dont need to close the file bcz tjis automatocally close the file
# Code :
# with open("path","mode") as f:
#     data = f.read()
#     print(data)


# we can delete the file using os module
# code :
# import os
# os.remove(file=path)

