class NumberStats():
    def __init__(self):
        self.sum = 0
        self.numbers = []
        self.asked_digits = []
        self.even_numbers = []
        self.odd_numbers = []
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

    def add_digit(self):
        while True:
            ask_the_user = int(input("Please type in integers (negative to stop): "))
            if ask_the_user < 0:
                break
            else:
                self.asked_digits.append(ask_the_user)


        sum_of_digits = sum(self.asked_digits)
        mean_of_digits = sum_of_digits / len(self.asked_digits)


        print(f"Sum of numbers: {sum_of_digits}")
        print(f"Mean of numbers: {mean_of_digits}")

    def calculate_sums(self):
        sum_of_even_numbers = 0
        sum_of_odd_numbers = 0

        for digits in self.asked_digits:
            if digits % 2 == 0:
                self.even_numbers.append(digits)
                sum_of_even_numbers += digits
            else:
                self.odd_numbers.append(digits)
                sum_of_odd_numbers += digits

        print(f"Sum of even numbers: {sum_of_even_numbers}")
        print(f"Sum of odd numbers: {sum_of_odd_numbers}")

if __name__ == "__main__":
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    stats.add_digit()
    stats.calculate_sums()



