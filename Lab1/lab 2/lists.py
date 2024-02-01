# example 1
mylist = ["apple", "banana", "cherry"]
# example 2
thislist = ["apple", "banana", "cherry"]
print(thislist)
# example 3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#example  4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#example  5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#example  6
list1 = ["abc", 34, True, 40, "male"]
#example  7
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#example  8
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#example  9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#example  10
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#example  11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#example  12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#example  13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#example  14
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#example  15
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#example  16

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#example  17
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#example  18
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#example  19
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#example  20
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#example  21
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#example  22
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#example  23
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#example  24
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#example  25
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#example  26
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#example  27
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#example  28

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#example  29
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#example  30
thislist = ["apple", "banana", "cherry"]
del thislist
#example  31
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#example  32
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#example  33
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#example  34
  list = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  #example  35

  i = i + 1
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#example  36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#example  37
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#example  38
newlist = [x for x in fruits if x != "apple"]
#example  39
newlist = [x for x in fruits]
#example  40
newlist = [x for x in range(10)]

#example  41
newlist = [x for x in range(10) if x < 5]
#example  42
newlist = [x.upper() for x in fruits]
#example  43
newlist = ['hello' for x in fruits]
#example  44
newlist = [x if x != "banana" else "orange" for x in fruits]
#example  45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#example  46
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#example  47
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#example  48
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#example  49
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#example  50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#example  51
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#example  52
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#example  53
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#example  54
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#example  55
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#example  56
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#example  57
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#EX 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#EX 2
fruits = ["apple", "banana", "cherry"]
fruits[0]="kids"
#EX 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#EX 4
fruits = ["apple", "banana", "cherry"]
fruits.insert (1,"lemon")
#EX 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#EX 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#EX 7

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#EX 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

