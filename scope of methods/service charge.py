class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
        self.__apply_service_charge()

    @property
    def account_info(self):
        return self.__name, self.__account_number, self.__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance: float):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance. Balance must be non-negative.")

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__apply_service_charge()

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__apply_service_charge()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def __apply_service_charge(self):
        if self.__balance > 0:
            self.__balance -= (self.__balance * 0.01)


if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)  # Should print 990.0 after service charge
    account.deposit(100)
    print(account.balance)  # Should print 1090.0
    account.balance = -500
