from random import randint
from art import logo


def guess_number(user_input, random_num):
    if user_input == random_num:
        return True
    elif user_input > random_num:
        return False
    elif user_input < random_num:
        return False


print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

difficulty_level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
is_game_over = False
RANDOM_NUMBER = randint(1, 100)

if difficulty_level == 'easy':
    attempts = 10
elif difficulty_level == 'hard':
    attempts = 5

while not is_game_over:
    print(f'You have {attempts} attempts remaining to guess the number.')
    user_guess = int(input('Make A Guess: '))
    is_correct_guess = guess_number(user_input=user_guess, random_num=RANDOM_NUMBER)
    is_wrong_guess = guess_number(user_input=user_guess, random_num=RANDOM_NUMBER)
    if is_correct_guess:
        print(f'You Got It! The Answer Was {RANDOM_NUMBER}')
        is_game_over = True
    elif not is_wrong_guess:
        attempts -= 1

        if attempts > 0 and user_guess > RANDOM_NUMBER:
            print('Too High.')
            print('Guess Again.')
        elif attempts > 0 and user_guess < RANDOM_NUMBER:
            print('Too Low.')
            print('Guess Again.')
        if attempts == 0:
            is_game_over = True
            print('You\'ve Run Out Of Guesses, You Lose')
