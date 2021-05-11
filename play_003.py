# Given a list, write a Python program to swap first and last element of the list.

def swap(arr):

    if len(arr) < 2 :
        return "Cant's swap"
    else:
        front_arr = []
        tail_arr = []

        front_arr.append(arr[0])
        tail_arr.append(arr[-1])

        new_list = tail_arr+arr[1:-1]+front_arr
        return new_list

def swap2(arr):

    if len(arr) < 2 :
        return "Cant's swap"
    else: 
        arr[0], arr[-1] = arr[-1], arr[0]

    return arr

def swap3(arr):

    if len(arr) < 2:
        return "Cant's swap"
    else:
        first = arr.pop(0)
        last = arr.pop(-1)

        arr.insert(0,last)
        arr.append(first)

        return arr

arr = [1,2,3,4,5,6,7]

print(swap3(arr))