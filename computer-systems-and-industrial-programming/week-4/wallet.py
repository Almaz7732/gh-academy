class Wallet:

    def __init__(self, balance):
        self.balance = balance

    def getCurrentBalance(self):
        return self.balance

    def updateBalance(self, newBalance):
        self.balance = newBalance
