class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    
    def Deposite(self, d):
        self.balance=self.balance+d

    def Withdrawal(self, w):
        if (self.balance < w):
            print('No enough funds in your account')
        else:
            self.balance=self.balance-w

    def display(self):
        print('Account number:', self.accountNumber)
        print('Account holder name:', self.name)
        print('Account balance:',self.balance)


p1=BankAccount(123450, 'Raj Patel', 2600)



p1.Withdrawal(4100)
p1.display()
























