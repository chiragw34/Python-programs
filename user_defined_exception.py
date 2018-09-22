class MyException(Exception):
    def __init__(self,arg):
        self.args=arg
        
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
print("1. num1/num2      2. num2/num1")
opt=int(input("enter the option:"))
try:
    if (opt==1):
            if (b==0):
                raise MyException("Error")
            else:
                print("num1/num2=",a/b)
    elif (opt==2):
            if (a==0):
                raise MyException("wtf")
            else:
                print("num2/num1=",b/a)
except MyException:
        print("divide by zero error!")
        print("please check your input")

        
finally:
    print("num1 is :",a,"   num2 is:",b)