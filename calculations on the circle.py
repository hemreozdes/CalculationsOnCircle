class Circle:
    pi=3.14
    def __init__(self,radius):
        self.r=radius
    def circumference(self):
        return 2*self.pi+self.r
    def area(self):
        return self.pi*(self.r**2)
r = int(input("Enter the radius:"))
c = Circle(r)
print(f"area = {c.area()} circumference = {c.circumference()}")