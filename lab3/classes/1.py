class stri():
    def __init__(self):
        self.string=""

    def getString(self):
        self.string=input()
    
    def printstring(self):
        print(self.string.upper())

a=stri()
a.getString()
a.printstring()