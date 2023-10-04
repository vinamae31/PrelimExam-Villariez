import math

class square():
    def __init__(self, area):
        self.a = area

    def area(self):
        return(self.a * self.a)

    def perimeter(self):
        return(self.a*4)

if __name__=='__main__':
    s = square (25)
    print(" Perimeter Of Square is equals to", + s.perimeter())
    print(" Area Of Square is equals to", + s.area())
    print(" Side Of The Square is 25")
    
