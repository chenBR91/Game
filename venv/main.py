
import user_class
import menu
import games.secretNumber
import games.rockPaperScissors
import games.hangman

from log.logFile import update_log, update_log_exit, update_log_start

import datetime


def main():
    update_log_start()

    list_all_users = []
    # create first gamer
    name = input('Hello please enter your name: ')
    list_all_users.append(create_user(name))
    # player first gamer
    play_user = list_all_users[0]

    while True:
        # print main menu
        menu.main_menu(play_user.name)

        try:
            selectMenu = int(input('Select an option from the menu: '))
            if selectMenu == 1:
                if __name__ == "__main__":
                    #run game rock Paper Scissors
                    games.rockPaperScissors.run_game(play_user)

            if selectMenu == 2:
                if __name__ == "__main__":
                    # run game hangman
                    games.hangman.run_game(play_user)

            elif selectMenu == 3:
                if __name__ == "__main__":
                    # run game secret Number
                    games.secretNumber.run_game(play_user)

            # add new gamer
            elif selectMenu == 4:
                name_user = input('Please enter your name: ')
                # find a gamer in the gamers list
                index_user = find_user(list_all_users, name_user)
                if index_user == -1:
                    # Not found gamer. create new user
                    play_user = create_user(name_user)
                    list_all_users.append(play_user)
                else:
                    play_user = list_all_users[index_user]

            elif selectMenu == 5:
                # send user scores to a text file
                send_txt_details(list_all_users)
                update_log_exit()
                # End program
                break


        except ValueError:
            print(ValueError)


def create_user(name):
    play_user = user_class.User(name)  # creat new uaer
    # log
    update_log(f'create a new user named: {play_user.name}')
    return play_user


def find_user(lst_users, name):
    for i in range(len(lst_users)):
        if lst_users[i].name == name:
            # return index of user
            return i
    # Not found user into the list
    return -1


# the function writes scores in the text file
def send_txt_details(users):
    file_name = format_time()
    with open(file_name, 'a') as f:
        for user in users:
            f.write(user.display_txt())


# the function return date and time the file was created
# format %d-%m-%y %h-%m
def format_time():
    today = datetime.datetime.now()
    return f'{today.day}-{today.month}-{today.year} {today.hour}-{today.minute}.txt'




if __name__ == "__main__":
    main()
