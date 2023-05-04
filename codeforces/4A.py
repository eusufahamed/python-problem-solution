import time
start_time = time.time()

def userInput():
    while True:
        weight = int(input('Enter watermelon weight: '))
        if 1<=weight<=100:
            break
        else:
            print('The watermelon weight must be greater than 1 and less then 100')

    return weight

weight = userInput()

if weight % 2 == 0:
    print('YES')
else:
    print('NO')
# w = int(input())
# if 1<=w<=100:
#     print("YNEOS"[(w%2)|(w<=2)::2])
# print("Process finished --- %s seconds ---" % (time.time() - start_time))

# print("YNEOS"[0::2]) # "YES"
# print("YNEOS"[1::2]) # "NO"


        