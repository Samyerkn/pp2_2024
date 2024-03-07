import os
path = input("Enter path: ")
#/Users/Samyerkn/lab6/dirandfiles/file_for_ex5.py as example
my_list = ["Divergent", "The Matrix", "The Hunger games"]
with open(path, 'w') as file:
    for element in my_list:
        file.write(str(element) + '\n')
        
print("List has been written to the file successfully.")
    