"""Linear Search"""
# Given an array arr[] of n elements, write a function to search a given element x in arr[].

def linear_search(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1

# variable declaration
arr = [2, 5, 8, 45, 62, 56, 4, 9, 10, 12, 32]
x = 56
n = len(arr)

result = linear_search(arr, n, x)
if (result == -1):
    print('Element is not present in list')
else:
    print('Element is present at index', result)
