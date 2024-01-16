#Part 1: the structure of the new class
class LunchCard():
    def __init__(self,balance: float):
        self.balance = balance
    #Part 2: paying for lunch
    def eat_lunch(self):
        if self.balance > 2.60:
            self.balance -= 2.60
        else:
            self.balance = self.balance
        return self.balance


    def eat_special(self):
        if self.balance > 4.60:
            self.balance -= 4.60
        else:
            self.balance = self.balance
        return self.balance
#Part 3: depositing money on the card
    def deposit_money(self,amount):
        if amount > 0:
            self.balance += amount
        return self.balance


    def __str__(self):
        return f"The balance is: {self.balance: .1f} euros"
if __name__ == "__main__":
    Peter = LunchCard(20)
    Grace = LunchCard(30)
    Peter.eat_special()
    Grace.eat_lunch()
    print(Peter)
    print(Grace)
    Peter.deposit_money(20)
    Grace.eat_special()
    print(Peter)
    print(Grace)
    Peter.eat_lunch()
    Peter.eat_lunch()
    Grace.deposit_money(50)
    print(Peter)
    print(Grace)