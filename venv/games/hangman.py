
# Hangman game

from log.logFile import update_log
import yaml
from random_word import RandomWords
from menu import hangman_title, feedback_game


def run_game(user):

    # log
    update_log(f'{user.name} play hangman game')

    # random word object
    r = RandomWords()
    # random word
    guess_random_word = str(r.get_random_word()).lower()

    chance = 6

    #print(guess_random_word)

    hangman_title(user.name, chance)

    if isGuessWord(guess_word=guess_random_word, counter_chance=chance):
        feedback_game('win')
        user.game2.win += 1
        update_log(f'{user.name}: win')
    else:
        feedback_game('lose')
        user.game2.loose += 1
        update_log(f'{user.name}: lose')

    user.game2.total += user.game2.loose + user.game2.win
    update_log(f'{user.name}: exit game')
    # game over



def isGuessWord(guess_word, counter_chance):
    length_word = len(guess_word)
    # create a list with a random word-length underline
    list_line_letter = list('_' * length_word)

    while counter_chance > 0:
        print('you have {} incorrect guesses left'.format(counter_chance))
        print_bottomLine(list_line_letter)

        input_letter = input('\nGuess letter: ')

        # find all indexes in a random word for letters guessed by the user
        index_letter = find_all(letter=input_letter, guess_word=guess_word)

        if index_letter == []: # empty
            # a character guessed by the user does not have the word random
            print('Sorry, wrong guess...')
            counter_chance -= 1
        else:
            print('Very Good!')
            # add letter to list in place of underline
            list_line_letter = update_guess_word(list_line_letter, input_letter, index_letter)
        # delete list for next round
        index_letter.clear()

        # if no underline character appears, all words are guessed
        if list_line_letter.count('_') == 0:
            # game over
            print(guess_word)
            print('successful')
            return True # win

    # game over
    return False # loose


def print_bottomLine(lst_line):
    for ch in lst_line:
        print(ch, end=' ')


def find_all(letter, guess_word):
    index_find = []
    for i in range(len(guess_word)):
        if letter == guess_word[i]:
            index_find.append(i)

    return index_find


def update_guess_word(lst_line, input_letter, index_letter):
    for index in index_letter:
        lst_line[index] = input_letter
    return lst_line