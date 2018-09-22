try:
    a=int(input("Enter number 1:-"))
    b=int(input("Enter number 2:-"))
    print(a/b)
          
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
try:
    b=input("Type y -")
    if (b!='y'):
        raise Exception
except Exception:
    print("please type correctly!!")
