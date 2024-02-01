class Wallet:
    def __init__(self):
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
        else:
            raise ValueError("The money cannot be negative")
if __name__ == '__main__':
    wallet = Wallet()
    print(wallet.money)

    wallet.money = 50
    print(wallet.money)

    wallet.money = -30
    print(wallet.money)