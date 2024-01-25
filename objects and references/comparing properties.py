class RealProperty:
    def __init__(self, rooms: int, square_meters: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm

    # Part 1: Is it bigger?
    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters
# Part 2: Price difference

    def price_difference(self, compared_to):
        return self.price_per_sqm > compared_to.price_per_sqm

# Part 3: Is it more expensive ?

    def more_expensive(self, compared_to):
        return (self.price_per_sqm * self.square_meters) > (compared_to.price_per_sqm * compared_to.square_meters)
if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))