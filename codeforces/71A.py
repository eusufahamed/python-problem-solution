import time
start_time = time.time()

num = int(input('number of words: '))
word_ls = []
for word in range(num):
    word = input('word: ')
    word_ls.append(word)

print(word_ls)

def abbre(l1: list) -> list:
    l2_les_10 = []
    l3_mor_10 = []
    abbres = []
    for word in l1:
        if len(word) < 10:
            l2_les_10.append(word)
        elif len(word) > 10:
            l3_mor_10.append(word)
    
    for item in l3_mor_10:
        first = item[0]
        middle = item[1:-1]
        last = item[-1]
        all = first + str(len(middle)) + last
        abbres.append(all)
    
    all_l1 = l2_les_10 + abbres

    return all_l1

all_item = abbre(word_ls)
for item in all_item:
        print(item)

print("Process finished --- %s seconds ---" % (time.time() - start_time))

# num = int(input())
# for _ in range(int(input())):
#     w = input()
#     s = len(w)-2
#     print([w,w[0]+str(s)+w[-1]][s>8])
