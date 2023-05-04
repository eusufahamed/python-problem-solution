# Write a Python program to check a list is empty or not

def check_list(l1: list) -> None:
    if len(l1) == 0:
        print('the list is empty')
    else:
        print('the list is not empty')

l1 = ['23', '67']
check_list(l1)