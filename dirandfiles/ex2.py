import os
path = input("Enter path: ")
#/Users/Samyerkn/lab6/dirandfiles/ex2.py as example
print(path)
print("Check for readability: ", os.access(path, os.R_OK))
print("Check for writability: ", os.access(path, os.W_OK))
print("Check for executability: ", os.access(path, os.X_OK))
print("Check for existence: ", os.path.exists(path))