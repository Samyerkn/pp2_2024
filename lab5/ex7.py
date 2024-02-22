import re

txt = "enter text"
x = ''.join(word.title() for word in txt.split('_'))
print(x)