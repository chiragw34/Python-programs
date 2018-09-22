x=input("enter number 1:-")
y=input("enter number 2:-")
print("x=",x,"     y=",y)
temp=x
x=y
y=temp
print("after swapping")
print("x=",x,"     y=",y)
z=int(input("enter a integer:-"))
if (z>0):
    print("given integer is positive")
elif (z<0):
    print("given integer is negative")
else:
    print("given integer is zero")
