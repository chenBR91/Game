
# Rock Paper Scissors game
import menu
from log.logFile import update_log
from menu import rock_paper_scissors_menu, feedback_game
from random import choice


def run_game(user):
    # init score
    win = 0
    loose = 0
    optin_play = ('rock', 'paper', 'scissors')

    # log
    update_log(f'{user.name} play rock paper and scissors game')

    while True:
        # print menu
        rock_paper_scissors_menu()

        try:
            option_menu = input('').lower()
            if option_menu in optin_play:
                # choose a random word from the list optin=('rock', 'paper', 'scissors')
                play_bot = choice(optin_play)
                # user selects a word rock/paper/scissors
                play_user = option_menu

                check_win = isPlay(play_user=play_user, bot=play_bot, user=user)


            elif option_menu == 'Quit' or option_menu == 'quit':
                # update user score
                user.game1.win += win
                user.game1.loose += loose
                user.game1.total = user.game1.win + user.game1.loose
                update_log(f'{user.name}: exit game')
                # game over
                break

            else:
                print('Invlid input, coose from {}'.format(optin_play))

        except ValueError:
            print(ValueError)



def isPlay(play_user, bot, user):
    # return True - user player win
    # return False - user player loose
    if play_user == 'rock' and bot == 'scissors':
        update_log(f'{user.name}: win')
        menu.feedback_game('win')
        user.game1.win += 1

    elif play_user == 'paper' and bot == 'rock':
        update_log(f'{user.name}: win')
        menu.feedback_game('win')
        user.game1.win += 1

    elif play_user == 'scissors' and bot == 'paper':
        update_log(f'{user.name}: win')
        menu.feedback_game('win')
        user.game1.win += 1

    elif play_user == bot:
        update_log(f'{user.name}: Tie')
        user.game1.win += 1
        print('Tie!')

    else:
        # bot win
        update_log(f'{user.name}: lose')
        menu.feedback_game('lose')
        user.game1.loose += 1


