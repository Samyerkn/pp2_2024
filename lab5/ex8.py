import re

txt = "enter text"
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)