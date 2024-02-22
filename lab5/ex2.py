import re
txt= input("enter text:")
x = re.findall("ab{2,3}", txt)
print(x)