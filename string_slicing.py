# initializing string
test_str = "416/2 Iqbal Rod, Shawrapara, Mirpur, Dhaka - 1216. Bangladesh."

# printing original string
print("The original string is : ", test_str)

# Splitting string into equal halves
res_first, res_second = test_str[:len(test_str)//2], test_str[len(test_str)//2:]

# printing result
print("The first part of string : ", res_first)
print("The second part of string : ", res_second)


# import math
# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1: return
#         yield start
#         start += len(sub)
#
#
# txt="I have done and what i can do."
# output = list (find_all(txt,' '))
# print(output)
# h_length=math.floor(len(output)/2)
# print(h_length)
#
# txt = txt[:output[h_length-1]] + '#' + txt[output[h_length-1] + 1:output[h_length+1]]+'#' + txt[output[h_length+1] + 1:]
#
# # txt = txt[:output[h_length-1]] + '#' + txt[output[h_length-1] + 1:]
# # txt = txt[:output[h_length+1]] + '#' + txt[output[h_length+1] + 1:]
#
#
# print(txt)
#
# output = txt.split('#')
# print(output)
