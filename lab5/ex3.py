import re

txt = "enter text"
x = re.findall("[a-z]+_[a-z]+", txt)
print(x)