tup=()
k=0
while(k<=4):
    print("======MENU======")
    print("1. Insertion")
    print("2. Display")
    print("3. Sort")
    print("4. Exit")
    k=int(input("Choose your option:-"))

    if(k==1):
        n=int(input("Enter the number of the elements to be inserted:"))
        for i in range(0,n):
            tup=tup[:i]+tuple(input("Enter the element:"))
            #count=count+1
    elif(k==2):
        print(tup)
    elif(k==3):
        tup=list(tup)
        for i in range(0,count):
            for j in range(0,count-1-i):
                if(tup[j]>tup[j+1]):
                    temp=tup[j]
                    tup[j]=tup[j+1]
                    tup[j+1]=temp
        tup=tuple(tup)
        
    else:
        break
