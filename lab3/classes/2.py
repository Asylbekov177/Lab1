class shape():
    def area(self):
        print(0)

class square(shape):
    def __init__(self, lenght):
        super().__init__()
        self.lenght=lenght
    def area(self):
        print(self.lenght**2)

class rectangle(shape):
    def __init__(self, width, lenght):
        super().__init__()
        self.width=width
        self.lenght=lenght

    def area(self):
        print(self.width*self.lenght)

square = square(7)
square.area()

rectangle = rectangle(7,9)
rectangle.area()
