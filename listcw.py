k=0
while (k<=6):
    print("**********Menu**********")
    print("1. separate odd even")
    print("2. merge and sort two list")
    print("3. update first element with x value and delete middle element")
    print("4. find min max ")
    print("5. add n strings to existing list check word  python is present in list")
    print("6. exit")
    k=int(input("enter your choice:-"))

    if(k==1):
        n=int(input("enter the number of members of list:-"))
        mylist = []
        evenlist=[]
        oddlist=[]
        for i in range(0,n):
            mylist.append(int(input("enter a number:")))
        print(mylist)

        for i in range(0,n):
            if(mylist[i]%2==0):
                evenlist.append(mylist[i])
            else:
                oddlist.append(mylist[i])
        print("Even list = ",evenlist)
        print("Odd list = ",oddlist)


    elif(k==2):
        list1=[]
        list2=[]
        n1=int(input("enter the number of members of list 1:-"))
        for i in range(0,n1):
            list1.append(input("enter a string:"))
        n2=int(input("enter the number of members of list 2:-"))
        for i in range (0,n2):
            list2.append(input("enter a string:"))
        list1.extend(list2)
        print(list1)
        n=n1+n2
        for i in range(0,n):
            for j in range(0,n-1-i):
                if(list1[j]>list1[j+1]):
                    temp=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=temp
        print(list1)

    elif(k==3):
        mylist=[]
        n=int(input("Enter the number of the members of the list:"))
        for i in range(0,n):
            mylist.append(input("enter a member:"))
        print(mylist)
        mylist[0]=input("enter the value of first member to be updated:")
        print("deleting middle element....")
        for i in range(n//2,n-1):
            mylist[i]=mylist[i+1]
        mylist.pop(n-1)
        print(mylist)

    elif(k==4):
        mylist=[]
        lmin,lmax=0,0
        n=int(input("Enter the number of the members of the list:"))
        for i in range(0,n):
            mylist.append(int(input("enter a member:")))
            if(i==0):
                lmax=mylist[i]
                lmin=mylist[i]
            if(lmax < mylist[i]):
                lmax=mylist[i]
            if(lmin > mylist[i]):
                lmin=mylist[i]
        print("maximum =",lmax,"  minimun =",lmin)
        
    elif(k==5):
        mylist=[]
        flag=0
        n=int(input("enter the number of strings to be added:-"))
        for i in range(0,n):
            mylist.append(input("enter a string:-"))
            if(mylist[i]=='python'):
                flag=1
        if(flag==1):
            print("python is present")
        else:
            print("python is not present")
        print(mylist)

    else:
        break
print("good bye")
    
