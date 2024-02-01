class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class Room:
    def __init__(self):
        self.persons_list = []

    def add(self, person: Person):
        self.persons_list.append(person)

    def is_empty(self):
        return len(self.persons_list) == 0

    def print_contents(self):
        print(
            f"There are {len(self.persons_list)} persons in the room, and their combined height is {sum(person.height for person in self.persons_list)}")
        for person in self.persons_list:
            print(f"{person.name} {person.height}(cm)")

    def shortest(self):
        if not self.persons_list:
            return "No persons in the room."

        shortest_person = min(self.persons_list, key=lambda x: x.height)
        return f"The shortest person is {shortest_person.name} with a height of {shortest_person.height}(cm)"
    def remove_shortest(self):
        if not self.persons_list:
            return None
        shortest_person = min(self.persons_list, key=lambda x: x.height)
        self.persons_list.remove(shortest_person)
        return shortest_person
if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()