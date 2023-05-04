# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.

def max_min(data):
    l = data[0]
    s = data[0]

    for num in data:
        if num > l:
            l = num
        elif num < s:
            s = num

    return l, s

result = max_min([0, 9, 39, 87, 8, -5, -1, 6])
print(result)
