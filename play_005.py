mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(type(("apple", "banana", "cherry")))
print(thislist)

"""

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.

"""

thislist = ["apple", "banana", "cherry"]
print(thislist[0:-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

if "orange" in thislist:
    print("hh")