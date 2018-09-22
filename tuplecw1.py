k=0
mylist=[]
while(k<=4):
    print("======MENU======")
    print("1. Insertion")
    print("2. Display")
    print("3. Sort")
    print("4. Exit")
    k=int(input("Choose your option:-"))
    if(k==1):
        n=int(input("Enter the number of the students:"))
        for i in range(0,n):
            name=input("Enter the name of student:")
            rno=int(input("Enter the roll number of student:"))
            sub1=int(input("Enter the marks of subject 1:"))
            sub2=int(input("Enter the marks of subject 2:"))
            sub3=int(input("Enter the marks of subject 3:"))
            total=(sub1+sub2+sub3)/3
            tup=(name,rno,total)
            mylist.append(tup)
    elif(k==2):
        print(mylist)
    elif(k==3):
        for i in range(0,n):
            for j in range(0,n-1-i):
                if(mylist[j][2]>mylist[j+1][2]):
                    temp=mylist[j]
                    mylist[j]=mylist[j+1]
                    mylist[j+1]=temp
    else:
        break
