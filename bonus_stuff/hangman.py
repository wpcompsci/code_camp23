import string
import random

# initialize the variables
words_list = []

with open('words.txt', 'r') as file:
    for line in file:
        words_list.append(line.strip('\n'))

word = random.choice(words_list)
blanks = []
for letter in word:
    blanks.append('_')
letters_available = list(string.ascii_lowercase)

# Play the game loop
while True:
    for blank in blanks:
        print(blank, end=' ')
    print()
    for letter in letters_available:
        print(letter, end=' ')
    guess = input('\nGuess a letter: ').lower()

    if guess in letters_available:
        letters_available.remove(guess)

        if guess in word:
            print('Correct!')
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
        else:
            print('Incorrect!')
    else:
        print('You already guessed that letter!')

    if '_' not in blanks:
        print('You win!')
        break

print(f'You guess the word. It was {word}!')