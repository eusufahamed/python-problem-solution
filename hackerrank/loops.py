# way 1 (long)
# number = int(input())
# if 1 <= number <= 20:
#     l1 = []

#     for num in range(number):
#         l1.append(num)

#     squares = [item**2 for item in l1]
    
#     for i in square:
#         print(i)

# way 2 (less)
number = int(input())
if 1 <= number <= 20:

    for num in range(number):
        print(num**2)
