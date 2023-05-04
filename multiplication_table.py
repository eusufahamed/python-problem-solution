def multiplication_table(num):
    for i in range(1, 11):

        print(num, 'X', i, '=', num * i)

num = int(input('Enter a Number: '))
print('Multiplication Table of', num)
multiplication_table(num)
