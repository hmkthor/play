# find the largest num in an array

arr = [10,20,30,40,50]

def largest(arr):
    n = len(arr)

    max = 0

    for i in range(0,n-1):
        if arr[i] > max:
            max = arr[i]
    
    return max



print(largest(arr))