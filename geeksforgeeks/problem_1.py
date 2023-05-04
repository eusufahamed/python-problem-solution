"""https://www.geeksforgeeks.org/python-program-to-build-flashcard-using-class-in-python/
In this article, we will see how to build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memorization. Flashcards usually have a question on one side and an answer on the other. Particularly in this article, we are going to create flashcards that will be having a word and its meaning.

Let’s see some examples of flashcard:

Example 1:

Approach :

Take the word and its meaning as input from the user.
Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
Now we create a function which can add the word and meaning and return string that contains the word and meaning.
Store the returned strings in a list named flash.
Use a while loop to print all the stored flashcards."""

class FlashCard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def addString(self):
        result = self.word + ' ( ' + self.meaning + ' )'
        return result

flash = []
print('Welcome to flashcard application')

while True:
    word = input('Enter the name you want to add flashcard: ')
    meaning = input('Enter the the meaning of the word: ')

    f = FlashCard(word, meaning)
    flash.append(f.addString())

    option = int(input('Enter 1, if you want add another flashcard: '))

    if not option:
        break

print('your flashcard')
for i in flash:
    print('>', i)
