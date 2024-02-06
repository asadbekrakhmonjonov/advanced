# Part 1: Item
class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}, {self.weight} (kg)'

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

# Part 2: Suitcase
class Suitcase:
    def __init__(self,maximum_weight: float):
        self.maximum_weight = maximum_weight
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)
    def print_items(self):
        for item in self.items:
            print(f'{item.name}: {item.weight} (kg)')
    def weight(self):
        return sum(item.weight for item in self.items)
    def heaviest_item(self):
        heaviest = max(self.items, key=lambda item: item.weight)
        return heaviest

    def __str__(self):
        total_weight = sum(item.get_weight() for item in self.items)
        if len(self.items) == 1:
            return f'{len(self.items)} item and {total_weight} kg'
        else:
            return f'{len(self.items)} items and {total_weight} kg'
class CargoHold:
    def __init__(self, maximum_weight: float):
        self.maximum_weight = maximum_weight
        self.on_hold = []
        self.space = self.maximum_weight
    def add_suitcase(self, suitcase: Suitcase):
       if suitcase.weight() <= self.maximum_weight:
           self.on_hold.append(suitcase)
           self.space -= suitcase.weight()
       else:
           print("no enough space")
    def __str__(self):
        return f'{len(self.on_hold)} space for {self.space} kg'
    def print_items(self):
        for suitcase in self.on_hold:
            suitcase.print_items()

if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()