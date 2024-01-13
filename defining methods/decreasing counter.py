class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value: ", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        return self.value

    def set_to_zero(self):
        self.value = 0
        return self.value

    def reset_original_value(self, new_value: int):
        self.value = new_value


if __name__ == "__main__":
    counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value(55)
    counter.print_value()
