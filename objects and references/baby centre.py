class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.total_weigh_ins = 0

        pass

    def weigh(self, person: Person):
        self.total_weigh_ins += 1
        return person.weight
    def weigh_ins(self):
        return self.total_weigh_ins
    def feed(self, person: Person):
        person.weight += 1
        return person.weight

if __name__ == '__main__':
    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    baby_centre = BabyCentre()
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")