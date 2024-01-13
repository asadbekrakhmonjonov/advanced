class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
peters_account =BankAccount("Peter Python",2000)
paulas_account =BankAccount("Paula Python",5000)
print(peters_account.name, peters_account.balance)
print(paulas_account.name, paulas_account.balance)
