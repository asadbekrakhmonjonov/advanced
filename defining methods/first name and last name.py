class Person():
    def __init__(self,name):
        self.name = name
    def return_first_name(self):
        self.first_name = self.name.split()[0]
        return self.first_name
    def return_last_name(self):
        self.last_name = self.name.split()[-1]
        return self.last_name
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())