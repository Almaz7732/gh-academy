import random


class NumberGame:
    def __init__(self, number=None):
        self.number = number if number is not None else random.randint(1, 100)
        self.limit = 10
        self.result = False

    def get_user_input(self, prompt):
        return int(input(prompt))

    def check_guess(self, guess):
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "too_low"
        else:
            return "too_high"

    def play(self):
        print('Number Guessing Game')
        print('You have 10 attempts')

        while self.limit > 0:
            try:
                user_input = self.get_user_input('Guess a number between 1 and 100: ')
            except ValueError:
                print('Please enter a valid number!')
                continue

            result = self.check_guess(user_input)

            if result == "correct":
                self.result = True
                break
            elif result == "too_low":
                print('Too low!')
            else:
                print('Too high!')

            self.limit -= 1

        if self.result:
            print('Correct!')
            return True
        else:
            print('Game over')
            return False


if __name__ == "__main__":
    game = NumberGame()
    game.play()