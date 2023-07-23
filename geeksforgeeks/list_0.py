# Python Program to count unique values inside a list

list_0 = [1, 2, 4, 2, 'abc', 8, 2.4]
list_result = []
count = 0

for item in list_0:
    if item not in list_result:
        count += 1
        list_result.append(item)

print('No of unique items are: ', count)