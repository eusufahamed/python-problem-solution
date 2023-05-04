sentence = str(input('Write a Sentence to Check the Vowel and Consonant: ')).lower()

checkvc = ''
for word in sentence.split():
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        checkvc += word
        checkvc += ' Vowel '
    else:
        checkvc += word
        checkvc += ' Consonant '

print(checkvc)
