import re

txt = "enter text"
x = re.findall("[A-Z][a-z]+", txt)
print(x)