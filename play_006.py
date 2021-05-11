"""
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(len(thislist))
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(len(thislist))
print(thislist)