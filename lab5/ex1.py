import re

txt = input ("enter text")
x = re.findall("ab*", txt)
print(x)