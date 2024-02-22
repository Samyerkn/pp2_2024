#1
print("Hello")
print('Hello')
#2
a = "Hello"
print(a)
#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#5
a = "Hello, World!"
print(a[1])
#6
for x in "banana":
  print(x)
  #7
  a = "Hello, World!"
print(len(a))
#8
txt = "The best things in life are free!"
print("free" in txt)
#9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #10
  txt = "The best things in life are free!"
print("expensive" not in txt)
#11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  #Slicing 1
  b = "Hello, World!"
print(b[2:5])
#Slicing 2
b = "Hello, World!"
print(b[:5])
#Slicing 3
b = "Hello, World!"
print(b[2:])
#Slicing 4
b = "Hello, World!"
print(b[-5:-2])
#Upper case1
a = "Hello, World!"
print(a.upper())
#Upper case2
a = "Hello, World!"
print(a.lower())
#Upper case3
a = " Hello, World! "
#Upper case4
a = "Hello, World!"
print(a.replace("H", "J"))
#Upper case5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# str conc.1
a = "Hello"
b = "World"
c = a + b
print(c)
# str conc.2
a = "Hello"
b = "World"
c = a + " " + b
#format1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#format2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#format3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#escape 1
txt = "We are the so-called \"Vikings\" from the north."

