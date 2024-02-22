import re

txt = "enter text"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
print(x)