"""Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other."""

def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(test_distinct([1, 2, 3, 4,]))
print(test_distinct([1, 2, 3, 4, 4]))
