mylist=[]
n=int(input("Enter the number of the members of the list"))
for i in range(0,n):
    mylist.append(input("enter a member"))
print(mylist)
mylist[0]=input("enter the value of first member to be updated:")
print("deleting middle element")
for i in range(n//2,n-1):
    mylist[i]=mylist[i+1]
mylist.pop(n-1)
print(mylist)
    
