import re

txt = "Hello, world. How are you?"
x = re.sub("[ ,.]", ":", txt)
print(x)