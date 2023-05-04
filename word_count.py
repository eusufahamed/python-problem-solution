sentence = str(input('Enter the Sentence: '))
wordlist = sentence.split()
print(len(wordlist))

worddictionary = {}
for word in wordlist:
    if word in worddictionary:
        worddictionary[word] = worddictionary[word] + 1
    else:
        worddictionary[word] = 1

    print(worddictionary)
