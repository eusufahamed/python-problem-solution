# write a function to find the unique characters of a string

def unique_char(arr):
    unique_char = []
    for char in arr:
        if char not in unique_char:
            unique_char.append(char)

    return unique_char

length = unique_char('Eusuf Ahamed')
print(length)
print(len(length))

