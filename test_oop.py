from first import BankAccount, PersistenceAccount, BankTransaction
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

class TestBankTransaction(unittest.TestCase):
    def setUp(self):
        self.BankTransaction = BankTransaction() 

    def test_dundor_method_del(self):
        obj_str = str(self.BankTransaction)
        del self.BankTransaction

        with open('transaction.txt', 'r') as f:
            lst_text = f.readlines()
        self.assertEqual(obj_str, lst_text[-1])

class TestPersistenceAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)
    
    def test_serialisation(self):
        PersistenceAccount.serialize(self.account)
        from_file = PersistenceAccount.deserialize()
        self.assertEqual(str(self.account), str(from_file))


if __name__ == '__main__':
    unittest.main()