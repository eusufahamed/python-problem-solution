# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

"""algorithm:

    decler variable l1, count
    loop through the l1
    compare first and last character of the item[0] == item[-1]"""


def fast_last_char_same(l1: str) -> int:
    count = []
    for str_item in l1:
        if len(str_item) > 2 and str_item[0] == str_item[-1]:
            count.append(str_item)

    return len(count)

l1 = ['abc', 'xyz', 'aba', '1221', 'a']
print(fast_last_char_same(l1))

