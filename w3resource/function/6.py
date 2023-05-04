# Write a Python function to check whether a number falls in a given range.

def check_number_range(n):
    if n in range(10, 20):
        print(f'the {n} is in range')
    else:
        print(f'the {n} is not in range')

check_number_range(30)

