x=input("enter a string:-")
y=x[::-1]
if (x==y):
    print("given string is palindorme")
else:
    print("given string is not a palindorme")
def fact(x):
    if(x==0):
        return 1
    else:
        return (x*fact(x-1))

x=int(input("enter a number:-"))
print("factorial of ",x," is ",fact(x))
