# Write a Python program to get the smallest number from a list.

"""algorithm:

    declar variables l1, small_number
    loop through the l1
    compair every item of the l1 and stor the smallest number from the l1 in small_number"""

def find_small_num(num: int) -> int:
    small_number = num[0]
    for item in num:
        if item < small_number:
            small_number = item
    
    return small_number

l1 = [2, 3, 4, 5, 6, 7, 8, 9, 0]
print(find_small_num(l1))