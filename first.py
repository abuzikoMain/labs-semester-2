from datetime import date
class BankAccount(object):
    def __init__(self, balance = 100):
        self.number = _next_number()
        self.balance = balance

        self.created_date = date.today()

    def deposit(self, amount):
        self.balance += amount

    def is_enough_to_withdraw(self, amount: int) -> bool:
        to_return = True if self.balance - amount > 0 else False
        return to_return
    
    def withdraw(self, amount):
        if self.is_enough_to_withdraw(amount):
            self.balance -= amount

    def transfer_from(self, account, amount):
        account.withdraw(amount)
        self.deposit(amount)

    def __str__(self):
        return 'number: {0}, balance: {1}, created date: {2}'.format(self.number, self.balance, self.created_date)

_next = 0

def _next_number():
    global _next
    _next += 1
    return _next

if __name__ == '__main__':
    ba = BankAccount(100)
    ba.deposit(50)
    print(ba)