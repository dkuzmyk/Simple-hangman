# Hangman!

import random
import sys

end = False
errors = 0

with open('dictionary2.txt') as f:
    dictionary = f.read().splitlines()

word = dictionary[random.randint(0, len(dictionary))]

# print(word)
print("Discover the word!")

listed = list(word)
hidden = list('_'*len(word))

while not end:

    if errors > 0:
        print('   o')
    if errors == 2:
        print('   | ')
    elif errors == 3:
        print('  /| ')
    if errors > 3:
        print('  /|\ ')
    if errors == 5:
        print('  / ')
    if errors > 5:
        print('  / \ ')
        print('Ops! You died')
        print('Word: {}'.format(word))
        end = True
        sys.exit()

    pog = "".join(hidden)
    print(pog)
    print('')

    inputStr = input('Enter your letter: ')
    if word.find(inputStr) != -1:
        print("Found {}!".format(inputStr))
    else:
        errors += 1

    for a in range(len(listed)):
        if inputStr == listed[a]:
            hidden[a] = listed[a]

    ending = "".join(hidden)
    if ending == word:
        print("You win!")
        end = True
