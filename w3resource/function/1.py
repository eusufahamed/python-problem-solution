# Write a Python function to find the Max of three numbers.

def max_num(num1: int, num2: int, num3: int) -> int:
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(max_num(50, 40, 100))