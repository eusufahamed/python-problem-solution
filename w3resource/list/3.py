# Write a Python program to get the largest number from a list.

l1 = [25, 28, 100, 500, 1, 47]
largest = l1[0]

for item in l1:
    if item > largest:
        largest = item

print(largest)