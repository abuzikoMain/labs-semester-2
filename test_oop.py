import unittest
from first import BankAccount, date

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_account_created(self):
        temp_date = date.today()
        test_balance = 99
        self.test_account = BankAccount(99)
        self.assertEqual(self.test_account, f'number: {1}, balance: {test_balance}, created date: {temp_date}')

    def test_counter_number_accounts_with_del(self):
        ...

    def test_counter_number_accounts(self):
        ...

    def test_update_account_balance(self):
        ...
    
    def test_invalid_update_account_balance(self):
        ...

    def test_invalud_account_created(self):
        ...
    
    def test_invalid_account_deposit(self):
        ...

    def test_account_deposit(self):
        test_balance = 150
        self.account.deposit(50)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_withdraw(self):
        ...

    def test_invalid_account_withdraw(self):
        ...


if __name__ == '__main__':
    unittest.main()