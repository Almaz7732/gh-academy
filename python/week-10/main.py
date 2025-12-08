

class BankAccount:
    name = None
    balance = 0

    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Successfully deposited {amount}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Successfully withdrawn {amount}"
        else:
            return 'Insufficient funds'

    def display_balance(self):
        return f"Balance {self.name}: {self.balance}"


if __name__ == "__main__":
    accountOne = BankAccount("Alex", 0)
    accountTwo = BankAccount("Adam", 0)

    print(accountOne.display_balance())
    print(accountTwo.display_balance())

    print("-" * 29)

    print(accountOne.deposit(100))
    print(accountTwo.deposit(100))

    print("-" * 29)

    print(accountOne.withdraw(80))
    print(accountTwo.withdraw(101))

    print("-" * 29)

    print(accountOne.display_balance())
    print(accountTwo.display_balance())



