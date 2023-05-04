# Write a Python program to clone or copy a list.

# l1 = ['hello', 22, 'game']
# l2 = []
# for item in l1:
#     l2.append(item)

# print(f'i am copy from l1: {l1} to l2: {l2}')

l1 = ['hello', 22, 'game']
l2 = list(l1)

print(f'i am copy from l1: {l1} to l2: {l2}')