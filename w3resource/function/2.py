# Write a Python function to sum all the numbers in a list.

def sum_list(l1: list) -> int:
    result = 0
    for num in l1:
        result += num

    return result

l1 = [8, 2, 3, 0, 7]
print(sum_list(l1))