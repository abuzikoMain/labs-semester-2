from datetime import date, datetime
import pickle

class PersistenceAccount(object):
    @staticmethod
    def serialize(account):
        with open('bank_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed
    @staticmethod
    def deserialize():
        with open('bank_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account

class BankTransaction(object):
    def __init__(self, amount = 100, type_transaction = 'test_transaction', old_value = 0, new_value = 100):
        self.when = datetime.today()
        self.amount = amount
        self.type_transaction = type_transaction
        self.old_value = old_value
        self.new_value = new_value

    def __str__(self):
        return 'type {0} | old amount {1} | new amount {2} | amount {3} | when {4}\n'\
            .format(self.type_transaction, self.old_value, self.new_value, self.amount, self.when)
   
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write(str(self))
        f.closed

class BankAccount(object):
    def __init__(self, balance = 0):
        self.number = _next_number()
        self.balance = balance
        self.queue = []
        self.created_at = date.today()

    @classmethod
    def create_bank_account(cls, value):
        return cls(value)

    def deposit(self, amount):
        self.balance += amount
        old_value = self.balance - amount
        self.queue.append(BankTransaction(amount=amount, type_transaction='deposit', \
                                           old_value=old_value, new_value=self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        old_value = self.balance + amount
        self.queue.append(BankTransaction(amount=amount, type_transaction='withdraw', \
                                           old_value=old_value, new_value=self.balance))

    def transfer_from(self, account, amount):
        account.withdraw(amount)
        self.deposit(amount)

    def get_transaction(self):
        for _ in range(len(self.queue)):
            item = self.queue.pop(0)
            print(item)

    def __str__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    
    def __repr__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)

class PersonalBankAccount(BankAccount):
    def __init__(self, balance = 0, name = None):
        super(PersonalBankAccount, self).__init__(balance)
        self.name = name

    def __str__(self):
        return 'number: {0}, balance: {1}, name: {2}'.format(self.number, 
        self.balance, self.name)
    
    def interest(self, rate):
        self.balance *= (1 + rate)

class OverdrawnBankAccount(PersonalBankAccount):
    def __init__(self, balance = 0, overdrawn = -1000):
        super(OverdrawnBankAccount, self).__init__(balance)
        self.overdrawn = overdrawn

    def __str__(self):
        return 'number: {0}, balance: {1}, name: {2}, overdrawn {3}'\
        .format(self.number, self.balance, self.name, self.overdrawn)
    
    def withdraw(self, amount):
        if self.balance - amount > self.overdrawn:
            self.balance -= amount
            old_value = self.balance + amount
            self.queue.append(BankTransaction(amount=amount, type_transaction='withdraw', \
                                           old_value=old_value, new_value=self.balance))
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

def test_withdraw(account):
    print(account)
    amount = int(input('enter amount to withdraw from number {0}:'.format(account.number)))
    account.withdraw(amount)
    print(account)

if __name__ == '__main__':
    person = PersonalBankAccount(100, 'Alex')
    person.interest(.3)
    print(person)
    oba = OverdrawnBankAccount(100)
    test_deposit(oba)
    test_withdraw(oba)