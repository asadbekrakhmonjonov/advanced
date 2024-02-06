class SavingsAccount:
    general_rate = 0.03

    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def add_interest(self):
        total_interest = SavingsAccount.general_rate + self.__interest_rate
        self.__balance += (self.__balance * total_interest)
    @property
    def balance(self):
        return self.__balance
if __name__ == '__main__':
    print("The general interest rate is", SavingsAccount.general_rate)

    account = SavingsAccount("12345", 1000, 0.05)
    # Add the total interest accrued to the balance on the account
    account.add_interest()
    print(account.balance)