# Part 1: The Present class
class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

# Part 2: The box class
class Box:
    def __init__(self):
        self.present_list = []

    def add_present(self, present: Present):
        self.present_list.append(present)

    def total_weight(self):
        return sum(present.weight for present in self.present_list)

    def __str__(self):
        return "\n".join(f"Present: {present.name}" for present in self.present_list)

# Example usage:
if __name__ == "__main__":
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)

    print("Box contents:")
    print(box)
