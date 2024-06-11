import unittest
from first import BankAccount, date

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_account_created(self):
        test_balance = 99
        test_account = BankAccount(test_balance)
        self.assertIsInstance(test_account, BankAccount)

    def test_invalid_account_created(self):
        test_account = BankAccount()
        self.assertRaises(TypeError)

    def test_counter_number_accounts_with_del(self):
        ...

    def test_counter_number_accounts(self):
        ...

    def test_update_account_balance(self):
        test_balance = 99
        test_deposit = 1
        test_account = BankAccount(99)
        test_account.deposit(test_deposit)
        self.assertEqual(test_account.balance, 100)
    
    def test_invalid_account_deposit_with_less_zero_int(self):
        test_balance = 99
        test_deposit = -1
        test_account = BankAccount(99)
        test_account.deposit(test_deposit)
        self.assertEqual(test_account.balance, 99)

    def test_invalid_update_account_balance_with_str(self):
        test_balance = 99
        test_deposit = '-1'
        test_account = BankAccount(test_balance)
        test_account.deposit(test_deposit)
        self.assertRaises(Exception)

    def test_account_transfer(self):
        test_balance = 99
        test_withdraw = 99
        test_account_1 = BankAccount(test_balance)
        test_account_2 = BankAccount(test_balance)
        test_account_2.transfer_from(test_account_1, test_withdraw)
        self.assertEqual(test_account_1.balance, 0)
        self.assertEqual(test_account_2.balance, 198)

    def test_invalid_account_transfer_with_less_zero_int(self):
        test_balance = 99
        test_withdraw = -1
        test_account_1 = BankAccount(test_balance)
        test_account_2 = BankAccount(test_balance)
        test_account_2.transfer_from(test_account_1, test_withdraw)
        self.assertEqual(test_account_1.balance, 99)
        self.assertEqual(test_account_2.balance, 99)

    def test_invalid_account_transfer_with_bigger_then_account_have(self):
        test_balance = 99
        test_withdraw = 101
        test_acc_1 = BankAccount(test_balance)
        test_acc_2 = BankAccount(test_balance)
        test_acc_2.transfer_from(test_acc_1, test_withdraw)
        self.assertEqual(test_acc_1.balance, 99)
        self.assertEqual(test_acc_2.balance, 99)
  
    def test_invalid_account_transfer_with_less_with_str(self):
        test_balance = 99
        test_withdraw = '101'
        test_account_1 = BankAccount(test_balance)
        test_account_2 = BankAccount(test_balance)
        test_account_2.transfer_from(test_account_1, test_withdraw)
        self.assertEqual(test_account_1.balance, 99)
        self.assertEqual(test_account_2.balance, 99)

if __name__ == '__main__':
    unittest.main()