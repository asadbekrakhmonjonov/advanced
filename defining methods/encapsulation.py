class BankAccount():
    def __init__(self,account_number:str,owner:str,balance:float,annual_interest:float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest
    def add_interest(self):
        self.balance += self.balance * self.annual_interest
    def withdraw(self,amount:float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)

if peters_account.withdraw(2000):
    print("The withdrawal was successful, the balance is now", peters_account.balance)
else:
    print("The withdrawal was unsuccessful, the balance is insufficient")

    # "Force" the withdrawal of 2000
    peters_account.balance -= 2000

print("The balance is now:", peters_account.balance)
