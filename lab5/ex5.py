import re

txt = "acb abb abbbb"
x = re.findall("a.*b", txt)
print(x)
