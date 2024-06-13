from datetime import date

class BankAccount(object):
    def __init__(self, balance = 0):
        self.number = _next_number()
        self.balance = balance
        self.created_at = date.today()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
    
    def transfer_from(self, account, amount):
        account.withdraw(amount)
        self.deposit(amount)

    def __str__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    
    def __repr__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    
_next = 0
def _next_number():
    global _next
    _next += 1
    return _next

def test_deposit(account):
    print(account)
    amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
    account.deposit(amount)
    print(account)

if __name__ == '__main__':
    ba = BankAccount(100)
    test_deposit(ba)