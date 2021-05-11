"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""

def swap(arr, pos1, pos2):

    if len(arr) < 2 :
        return "A list should have more than one element."
    else:
        arr[pos1-1], arr[pos2-1] = arr[pos2-1], arr[pos1-1]

    
    return arr

arr = [23,65,19,90]

print(arr)
print(swap(arr,2,3))