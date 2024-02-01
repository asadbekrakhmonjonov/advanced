class Car:
    def __init__(self):
        self.__amount_of_petrol = 0
        self.__odometer = 0
    def fill_up(self):
        if self.__amount_of_petrol == 0:
            self.__amount_of_petrol += 60
        return self.__amount_of_petrol
    def drive(self, km: int):
        self.__odometer += km
        self.__amount_of_petrol -= km
        if self.__odometer >= 60:
            self.__odometer = 60
            self.__amount_of_petrol = 0


    def __str__(self):
        return f'Car: odometer reading {self.__odometer} km, petrol reamining {self.__amount_of_petrol} litres'
if __name__ == '__main__':
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)