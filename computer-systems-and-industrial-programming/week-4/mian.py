from wallet import Wallet

class Main:
    def __init__(self):
        firstBalance = Wallet(10)
        print(firstBalance.getCurrentBalance())

        firstBalance.updateBalance(25)
        print(firstBalance.getCurrentBalance())



main = Main()
