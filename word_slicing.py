import math
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


txt="I have done and what i can do."
output = list (find_all(txt,' '))
print(output)
h_length=math.floor(len(output)/2)
print(h_length)

txt = txt[:output[h_length-1]] + '#' + txt[output[h_length-1] + 1:output[h_length+1]]+'#' + txt[output[h_length+1] + 1:]

# txt = txt[:output[h_length-1]] + '#' + txt[output[h_length-1] + 1:]
# txt = txt[:output[h_length+1]] + '#' + txt[output[h_length+1] + 1:]


print(txt)

output = txt.split('#')
print(output)
