class Recording:
    def __init__(self, length: int):
        self.__length = length
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length):
        self.__length = length
        if length < 0:
            raise ValueError("The number is below zero")
if __name__ == '__main__':
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
