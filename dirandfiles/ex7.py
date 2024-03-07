file1 = "#/Users/Samyerkn/lab6/dirandfiles/file_for_ex7.py"
file2 = "#/Users/Samyerkn/lab6/dirandfiles/file_for_ex7.py.py"
#/Users/Samyerkn/lab6/dirandfiles/file_for_ex7.py
with open (file1, 'r') as src:
    with open (file2, 'w') as copy:
        for i in src:
            copy.write(i)