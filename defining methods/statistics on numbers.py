class NumberStats():
    def __init__(self):
        self.sum = 0
        self.numbers = []
    def add_number(self,number: int):
        self.numbers.append(number)
    def count_numbers(self):
        return len(self.numbers)
    def get_sum(self):
        for number in self.numbers:
            self.sum += number
        return self.sum
    def average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
