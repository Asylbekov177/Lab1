import math
class point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def show(self):
        print(self.x, ";", self.y, sep="")

    def move(self,x,y):
        self.x=x
        self.y=y

    def dist(self, p2):
        print(math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2))


a=point(1,1)
a.show()
a.move(2,2)
a.show()
b=point(2,2)
a.dist(b)
