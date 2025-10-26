import unittest
import sys

sys.path.insert(1, '../../python/week-5')
import game


class TestNumberGame(unittest.TestCase):

    def test_check_guess_correct(self):
        test_game = game.NumberGame(number=50)
        result = test_game.check_guess(50)
        self.assertEqual(result, "correct")

    def test_check_guess_too_low(self):
        test_game = game.NumberGame(number=50)
        result = test_game.check_guess(30)
        self.assertEqual(result, "too_low")

    def test_check_guess_too_high(self):
        test_game = game.NumberGame(number=50)
        result = test_game.check_guess(70)
        self.assertEqual(result, "too_high")

    def test_game_initialization(self):
        test_game = game.NumberGame(number=42)
        self.assertEqual(test_game.number, 42)
        self.assertEqual(test_game.limit, 10)
        self.assertFalse(test_game.result)


if __name__ == '__main__':
    unittest.main()