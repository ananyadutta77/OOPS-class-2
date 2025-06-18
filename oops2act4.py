class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def rectangle_area(self):
        return self.length*self.breadth
newRect=rectangle(12,10)    
print(newRect.rectangle_area())

class square():
    def __init__(self,s):
        self.side=s
    def square_area(self):    
        return self.side**2
sq=square(4)   
print(sq.square_area())


