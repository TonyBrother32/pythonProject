class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        result = self.__width*self.__length*25*5/1000
        print(f"{result} т")


highway = Road(100, 50)
highway.weight()
