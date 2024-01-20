class Person:
    def __init__(self,name: str, height:int):
        self.name = name
        self.height = height
class Attraction:
    def __init__(self,name: str, min_height:int):
        self.visitors = 0
        self.name = name
        self.min_height = min_height
    def admit_visitor(self, person: Person):
        if person.height >= self.min_height:
            self.visitors += 1
            print(f"{person.name} got on board")
        else:
            print(f"{person.name} was too short")
    def __str__(self):
        return f"{self.name} ({self.visitors} visitors)"
if __name__ == "__main__":
    rollercoaster = Attraction("Rollercoaster", 120)
    jared = Person("Jared", 172)
    alice = Person("Alice", 105)

    rollercoaster.admit_visitor(jared)
    rollercoaster.admit_visitor(alice)

    print(rollercoaster)