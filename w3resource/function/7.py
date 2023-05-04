# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def find_up_lo(str: str):

    d = {'up_char': 0, 'lo_char': 0}

    for char in str:
        if char.isupper():
            d['up_char'] += 1
        
        if char.islower():
            d['lo_char'] += 1
    print(f'no. of {d["up_char"]} characters')
    print(f'no. of {d["lo_char"]} characters')

print(find_up_lo('The quick Brow Fox'))
