class maths:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,x,y):
        return (x+y)
    def sub(self,x,y):
        return (x-y)
    def mult(self,x,y):
        return (x*y)
    def ndiv(self,x,y):
        return (x//y)
    def disp(self):
        print(self)

class gpu(maths):
    def __init__(self,x,y):
        super().__init__(x,y)

    def fdiv(self,x,y):
        return (x/y)

    def add(self,x,y,z=None):
        if z is None:
            return maths.add(self,x,y)
        else:
            return (x+y+z)

x=int(input("enter number 1:"))
y=int(input("enter number 2:"))

p2=gpu(x,y)
print("Division from parent class:-",p2.ndiv(x,y))
print("Division from child class:-",p2.fdiv(x,y))
print("Add method from child class:-",p2.add(x,y,3))
print("Add method from parent class:-",p2.add(x,y))

    
