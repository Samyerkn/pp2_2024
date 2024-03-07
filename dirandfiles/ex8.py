import os
path = input("Enter path for your file: ")
#/Users/Samyerkn/lab6/dirandfiles/file_for_ex7.py
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File successfully deleted!")
else:
    print("File not found!")