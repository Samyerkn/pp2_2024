import re

txt = "enter text"
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
print(x)
