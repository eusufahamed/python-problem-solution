# Write a Python program to find the list of words that are longer than n from a given list of words.

num = int(input('give a number: '))
l1 = ['information', 'hello', 'world', 'hi', 'impossible', 'goodbye', 'good', 'goodday']
l2 = []
for item in l1:
    if len(item) > num:
        l2.append(item)

print(l2)
