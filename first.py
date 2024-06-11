class BankAccount(object):
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    
if __name__ == '__main__':
    ba = BankAccount(1, 100)
    ba.deposit(50)
    print(ba.balance)