print("*****inside module_fibo*****")

#n=int(input("enter the number of terms of fibonacci series"))
def fibo(n):
    a=0
    b=1
    mylist=[a,b]
    for i in range(0,n):
        c=a+b
        a=b
        b=c
        mylist.append(c)
    print(mylist)
print("*****module_fibo ended*****")
