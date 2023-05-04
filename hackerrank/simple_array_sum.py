l1_size = int(input())
l1 = input().split()

def simpleArraySum(ar):
    total = 0
    if l1_size == len(ar):
        for item in ar:
            total += int(item)

        return total

print(simpleArraySum(l1))
