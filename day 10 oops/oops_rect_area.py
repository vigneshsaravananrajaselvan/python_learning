class reactangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area (self):
        print("Area :",self.length*self.width)
a1=reactangle(12,25)
a1.area()