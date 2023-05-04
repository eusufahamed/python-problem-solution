# write a function to extract number from string and addition the number

def extract_int_and_add(holestring):
    total = 0
    number = []
    splited = holestring.split(' ')
    for num in splited:
        if num.isdigit():
            number.append(int(num))

    for add_num in range(len(number)):
        total += number[add_num]


    return total

print(extract_int_and_add('apple 2 banana 4 orange 14'))

