class CreditCard:
    def __init__(self, number: str, name: str, balance: float):
        self.__number = number
        self.name = name
        self.__balance = balance
    def deposit_money(self, amount: float):
        if amount > 0:
            self.__balance += amount
    def withdraw_money(self, amount: float):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
    def retrieve_balance(self):
        return self.__balance
if __name__ == '__main__':
    card = CreditCard("123456", "Randy Riches", 5000)
    print(card.retrieve_balance())
    card.deposit_money(100)
    print(card.retrieve_balance())
    card.withdraw_money(500)
    print(card.retrieve_balance())
    # The following will not work because the balance is not sufficient
    card.withdraw_money(10000)
    print(card.retrieve_balance())
