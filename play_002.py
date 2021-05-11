#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

def rotates(arr, d, n):

    new_arr = arr[n:d] + arr[0:n]

    return new_arr

arr = [1,2,3,4,5,6,7]

print(rotates(arr,len(arr),2))