'''
Guess The Word Game: A simple word guessing game.
Try to guess the word letter by letter within a limited number of attempts.
'''
import random

print('\n+-------------------------+')
print('|**** Guess The Word! ****|')
print('+-------------------------+')

word_categories = {
    'fruit': [
        'apple', 'banana', 'cherry', 'grape', 'kiwi',
        'mango', 'orange', 'peach', 'pear', 'plum',
        'watermelon', 'strawberry'
    ],
    'animal': [
        'elephant', 'tiger', 'kangaroo', 'giraffe', 'alligator',
        'zebra', 'lion', 'hippopotamus', 'crocodile', 'gorilla',
        'chimpanzee'
    ],
    'city': [
        'paris', 'london', 'berlin', 'tokyo', 'newyork',
        'losangeles', 'sydney', 'toronto', 'dubai', 'rome',
        'madrid', 'moscow'
    ],
    'programming': [
        'python', 'javascript', 'java', 'ruby', 'perl',
        'swift', 'kotlin', 'typescript', 'cplusplus', 'go',
        'rust'
    ],
    'color': [
        'red', 'blue', 'green', 'yellow', 'purple',
        'orange', 'pink', 'brown', 'black', 'white',
        'gray'
    ],
    'adjective': [
        'tall', 'beautiful', 'pretty', 'smelly', 'long',
        'short', 'smart', 'ugly', 'fat', 'slow',
        'sweet', 'small', 'dangerous', 'dear', 'angry'
    ]
}

print("\nWelcome to Guess the Word!\n")

def choose_category():
    '''Prompt the user to choose a category'''
    print('\nChoose one of these categories:')
    for category in word_categories:
        print(f'-{category}')
    while True:
        chosen_category = input('\nEnter a category: ').lower()
        if chosen_category in word_categories:
            return  chosen_category
        print('invalid category, Please try again.')

def current_state(attempts_left, guessed_word, guessed_letters):
    '''Display the current state of the game.'''
    print(f'\nCurrent word: {" ".join(guessed_word)}')
    print(f'Attempts left: {attempts_left}')
    print(f'Guessed letters: {", ".join(guessed_letters)}\n')

def guess_the_word():

    '''Main function to run the Guess the Word game.'''

    chosen_category = choose_category()
    chosen_word = random.choice(word_categories[chosen_category])

    guessed_word = ['_'] * len(chosen_word)
    attempts_left = 6
    guessed_letters = []

    current_state(attempts_left, guessed_word, guessed_letters)

    while attempts_left > 0 and '_' in guessed_word:
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
            attempts_left -= 1
            print(f'The letter {guess} is not in the word.')

        current_state(attempts_left, guessed_word, guessed_letters)

    if '_' not in guessed_word:
        print('+------------------------+')
        print('|****Congratulations!****|')
        print('+------------------------+')
        print(f'\nYou guessed the word: {chosen_word.upper()}\n')
    else:
        print('+---------------+')
        print('|   GAME OVER   |')
        print('+---------------+')
        print(f'\nYou ran out of attempts. The word was: {chosen_word.upper()}\n')

if __name__ == "__main__":
    guess_the_word()
