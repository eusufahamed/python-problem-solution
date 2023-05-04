# Write a Python program to remove duplicates from a list.

def remv_dup(l1: list) -> list:
    new_l1 = []

    for item in l1:
        if item not in new_l1:
            new_l1.append(item)

    return new_l1

l1 = [25, 25, 'aa', 'bb', 'aa']
print(remv_dup(l1))