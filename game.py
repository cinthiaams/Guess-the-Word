'''
Guess The Word Game: A simple word guessing game.
Try to guess the word letter by letter within a limited number of attempts.
'''

print('+-----------------------+')
print('|*** Guess The Word! ***|')
print('+-----------------------+')

CHOSEN_WORD = 'programming'

guessed_word = ['_'] * len(CHOSEN_WORD)
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

    while ATTEMPTS_LEFT > 0 and '_' in guessed_word:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single alphabetical character.')
            continue

        if guess in guessed_letters:
            print('You have already guessed that letter. Try again.')
            continue

        guessed_letters.append(guess)

        if guess in CHOSEN_WORD:
            for index, letter in enumerate(CHOSEN_WORD):
                if letter == guess:
                    guessed_word[index] = guess

        else:
            ATTEMPTS_LEFT -= 1
            print(f'The letter {guess} is not in the word.')

        current_state()

    if '_' not in guessed_word:
        print(f'Congratulations, you guessed the word: {CHOSEN_WORD}')
    else:
        print(f'Sorry, you ran out of attempts. The word was: {CHOSEN_WORD}')

guess_the_word()
