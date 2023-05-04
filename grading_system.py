# Python Program - Calculate Grade of a Student

print("Enter 'x' for exit.\nEnter marks obtained in 5 subjects: ")

mark1 = input()
if mark1 == 'x':
    exit()
else:
    mark1 = int(mark1)
    mark2 = int(input())
    mark3 = int(input())
    mark4 = int(input())
    mark5 = int(input())
    sum   = mark1 + mark2 + mark3 + mark4 + mark5
    avarage = sum / 5
    if avarage >= 80 and avarage <= 100:
        print('You got A+')
    elif avarage >= 75 and avarage < 80:
        print('You got A')
    elif avarage >= 70 and avarage < 75:
        print('You got A-')
    elif avarage >= 65 and avarage < 70:
        print('You got B+')
    elif avarage >= 60 and avarage < 65:
        print('You got B')
    elif avarage >= 55 and avarage < 60:
        print('You got B-')
    elif avarage >= 50 and avarage < 55:
        print('You got C+')
    elif avarage >= 45 and avarage < 50:
        print('You got C')
    elif avarage >= 40 and avarage < 45:
        print('You got D')
    else:
        print('Sorry! You faild with F')
