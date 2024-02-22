#1
x = 5
y = "John"
print(x)
print(y)
#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#4var
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#5Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#6Output Variables
x = "Python is awesome"
print(x)
#7output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#8output Variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#9output Variables
x = 5
y = 10
print(x + y)
#10output Variables
x = 5
y = "John"
print(x, y)
#11output Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#12output Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#13output Variables
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#14output Variables
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#15output Variables
