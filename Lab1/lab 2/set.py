thisset = {"apple", "banana", "cherry"}
print(thisset)



thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}


myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)



  set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

  #Ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")