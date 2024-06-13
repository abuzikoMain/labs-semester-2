from first import BankAccount
import unittest
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_account_deposit(self):
        test_balance = 150
        self.account.deposit(50)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_deposit(self):
        test_balance = 50
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, test_balance)

    def test_account_deposit(self):
        test_balance = 0
        test_account = BankAccount()
        self.assertEqual(test_account.balance, test_balance) 

    def test_account_str(self):
        self.assertEqual(str(self.account), 'number: {0}, balance: {1}'.format(self.account.number, self.account.balance))       

    def test_account_number(self):
        self.assertEqual(self.account.number, 3)

if __name__ == '__main__':
    unittest.main()