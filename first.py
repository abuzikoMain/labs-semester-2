from datetime import date
import uuid

class BankAccount(object):
    def __init__(self, balance = 100):
        self.number = _next_number()
        self.balance = balance
        self.id = uuid.uuid4()
        self.created_date = date.today()

    def deposit(self, amount):
        if self.is_integer_and_positive(amount):
            self.balance += amount

    def is_enough_to_withdraw(self, amount: int) -> bool:
        to_return = True if self.balance - amount >= 0 else False
        return to_return
    
    def is_integer_and_positive(self, amount):
        to_return = True if isinstance(amount, int) and amount > -1 else False
        return to_return

    def withdraw(self, amount):
        if self.is_integer_and_positive(amount):
            if self.is_enough_to_withdraw(amount):
                self.balance -= amount
                return True
        return False

    def transfer_from(self, account, amount):
        liq = account.withdraw(amount)
        if liq is True:
            self.deposit(amount)

    def __repr__(self):
        return 'number: {0}, balance: {1}, created date: {2}'.format(self.number, self.balance, self.created_date)

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