a = int(input("enter the number A:"))
b = int(input("enter the number B:"))
c = int(input("enter the number C:"))
d = int(input("enter the number D:"))
ans = 0
for i in range(0,d):
    if(i%a is 0):
        ans = ans + 1
    elif(i%b is 0):
        ans = ans + 1
    elif(i%c is 0):
        ans = ans + 1
    
print(ans-1)
