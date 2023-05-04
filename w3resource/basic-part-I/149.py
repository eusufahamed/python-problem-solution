# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

# Function
def sum_of_cube(num):
    # smaller than the specified number
    num -= 1
    # result of sum
    sum = 0
    while num > 0:
        sum += num * num * num
        num -= 1

    return sum

finalResult = sum_of_cube(6)
print(finalResult)
