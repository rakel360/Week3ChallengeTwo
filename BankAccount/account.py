class BankAccount:
    def __init__(self, is_active=True):
        self.balance=0
        self.is_active=is_active
        

    def get_balance(self):
        if self.is_active==False:
            raise ValueError('ValueError')
        return self.balance


    def open(self):
        self.balance=0


    def deposit(self, amount):
        if self.is_active==False or amount<0:
            raise ValueError('ValueError')
        self.balance +=amount
        print ("You have deposited " + str(amount) + ", your current balance is now " + str(self.balance))
        
        

    def withdraw(self, amount):
        if amount<0 or amount>self.balance or self.is_active==False:
            raise ValueError('ValueError')
        self.balance-=amount
        print("You have withdrawn " + str(amount) + ", your balance is now " + str(self.balance))
                    
        
    def close(self):
        self.is_active=False

# account=BankAccount()

# account.deposit(100)
# account.deposit(50)
# account.withdraw(20)
# account.withdraw(30)
# account.withdraw(20)
# account.deposit(20)