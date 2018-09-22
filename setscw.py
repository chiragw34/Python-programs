k=0
while (k<=4):
    print("======MENU======")
    print("1. Read two strings")
    print("2. Display common elements")
    print("3. Display commmon letters")
    print("4. Exit")
    k=int(input("Enter your choice:-"))

    if(k==1):
        s1=input("Enter string 1:-")
        s2=input("Enter string 2:-")
        print("String 1:-",s1)
        print("String 2:-",s2)

    elif(k==2):
        print(list(set(s1.split())&set(s2.split())))
    elif(k==3):
        print(set(s1)&set(s2))
    else:
        break
    
        
