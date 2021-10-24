
# Guess Secret Number game

import random
from menu import guess_number_menu, feedback_game
from log.logFile import update_log


def run_game(user):

    # log
    update_log(f'{user.name} play secret number guess game')

    # print menu of guess game
    guess_number_menu() # or menu.guess_number_menu

    if start():
        user.game3.win += 1
        update_log(f'{user.name}: win')
        feedback_game('win')
    else:
        user.game3.loose += 1
        update_log(f'{user.name}: lose')
        feedback_game('lose')


    user.game3.total += user.game3.loose + user.game3.win
    update_log(f'{user.name}: exit game')
    # game over



def start():
    # init
    attempts = 5
    attempt = 0

    # cpu random number 1-100
    secret_number = random.randint(1, 100)

    while attempts > 0 or secret_number == number_guess:
        try:
            print('you have {} guess left'.format(attempts))
            number_guess = int(input('what is your guess? '))

            # decrement chance
            attempts -= 1

            if isGuess(playerGuess=number_guess, secret_number=secret_number, chance=attempts):
                # Game over
                return True # win

        except ValueError:
            print('please insert a number type integer!')

    # Game over
    return False # loose



def isGuess(playerGuess, secret_number, chance):
    if playerGuess == secret_number:
        print('Successful guessing!')
        return True
    elif chance == 0:
        print('oops the secret number is: {}'.format(secret_number))
        return False
    elif secret_number > playerGuess:
        print('the secret number is above user guess')
    elif playerGuess > secret_number:
        print('the secret number is below user guess')
    return False
    pass
