# user management

class User():
    def __init__(self, name):
        self.name = name
        self.game1 = User_rock('rock paper scissors') # rock
        self.game2 = User_hangman('hangman') # hangman
        self.game3 = User_guess('guess secret number') # guess
        self.user_games = {'rock paper scissors': self.game1, 'hangman': self.game2, 'guess secret number': self.game3}
        #user_games??

    def display_txt(self):
        return f'{self.name}\n{self.game1}\n{self.game2}\n{self.game3}\n\n'



class User_rock():
    def __init__(self, title):
        self.title = title
        self.win = 0
        self.loose = 0
        self.total = 0


    def __str__(self):
        return '{}\nwin: {}\t| lose: {}\t| total games played: {}'.format(self.title, self.win, self.loose, self.total)



class User_hangman():
    def __init__(self, title):
        self.title = title
        self.win = 0
        self.loose = 0
        self.total = 0


    def __str__(self):
        return '{}\nwin: {}\t| lose: {}\t| total games played: {}'.format(self.title, self.win, self.loose, self.total)



class User_guess():
    def __init__(self, title):
        self.title = title
        self.win = 0
        self.loose = 0
        self.total = 0


    def __str__(self):
        return '{}\nwin: {}\t| lose: {}\t| total games played: {}'.format(self.title, self.win, self.loose, self.total)

