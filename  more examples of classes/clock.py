class Clock():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
            self.second += 1
    def set(self,hour,minute):
        self.hour = hour
        self.minute = minute
        self.second = 0
    def __str__(self):
        return f'{self.hour: 03}:{self.minute: 03}:{self.second: 03}'
if __name__ == '__main__':
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.set(12,5)
    print(clock)


