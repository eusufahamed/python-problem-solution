# Write a Python function that takes two lists and returns True if they have at least one common member.

def list_item_match(l1: list, l2: list) -> bool:
    for item in l1:
        if item in l2:
            return True
        return False

l1 = ['hello', 3, 'hi', 1]
l2 = [2, 'hii', 4]

print(list_item_match(l1, l2))
