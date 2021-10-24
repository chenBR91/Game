# test code

import unittest
import games.rockPaperScissors


class TestCalc(unittest.TestCase):
    def test_add(self):
        optin = ('rock', 'paper', 'scissors')
        self.assertEqual(games.rockPaperScissors.get_option(optin), 'rock')




if __name__ == "__main__":
    unittest.main()