'''
Guess The Word Game: A simple word guessing game.
Try to guess the word letter by letter within a limited number of attempts.
'''
import random

print('+-----------------------+')
print('|*** Guess The Word! ***|')
print('+-----------------------+')

word_list = ['programming', 'watermelon', 'water', 'elephant', 'music', 'portugal']
chosen_word = random.choice(word_list)

guessed_word = ['_'] * len(chosen_word)
ATTEMPTS_LEFT = 6
guessed_letters = []

def current_state():
    '''Display the current state of the game.'''
    print(f'\nCurrent word: {" ".join(guessed_word)}')
    print(f'Attempts left: {ATTEMPTS_LEFT}')
    print(f'Guessed letters: {", ".join(guessed_letters)}\n')

def guess_the_word():
    '''Main function to run the Guess the Word game.'''
    global ATTEMPTS_LEFT # pylint: disable=global-statement

    print("\nWelcome to Guess the Word!\n")
    print(f'\nCurrent word: {" ".join(guessed_word)}\n')

    while ATTEMPTS_LEFT > 0 and '_' in guessed_word:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single alphabetical character.')
            continue

        if guess in guessed_letters:
            print('You have already guessed that letter. Try again.')
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[index] = guess

        else:
            ATTEMPTS_LEFT -= 1
            print(f'The letter {guess} is not in the word.')

        current_state()

    if '_' not in guessed_word:
        print('+------------------------+')
        print('|****Congratulations!****|')
        print('+------------------------+')
        print(f'\nYou guessed the word: {chosen_word.upper()}\n')
    else:
        print('...SOoooOORRRrrrYYyyy...')
        print(f'\nYou ran out of attempts. The word was: {chosen_word.upper()}\n')

guess_the_word()
