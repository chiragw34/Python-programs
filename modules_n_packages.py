a. WAP to implement a module and import the modules
b. WAP to implement a package and import the packages
MODULE:
def stack(l1,n):
	 if n==1:
		 i=int(input("ENTER THE ELEMENT TO BE PUSHED INTO THE STACK:"))
		 l1.append(i)
	 elif n==2:
		print("ELEMENT POPPED OUT IS ",l1.pop()
	 elif n==3:
		print("ELEMENT AT TOP OF STACK IS ",l1[-1]
	 elif n==4:
		print("ELEMENTS OF STACK ARE:")
		for i in range(0,len(l1)):
			print(l1[i],end=" ")


#MODULE IMPORTED IN PROGRAM:
import teststack
a=1
l1=[]
while a==1:
	 print("\n1:PUSH 2:POP 3:PEEP 4:DISPLAY")
	 n=int(input("ENTER WHICH STACK OPERATION TO PERFORM:"))
	 if n<=4:
		teststack.stack(l1,n)
	 a=1
	 a=int(input("\nPRESS 1 TO CONTINUE 0 TO EXIT:"))

 OUTPUT:
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:1
ENTER THE ELEMENT TO BE PUSHED INTO THE STACK:5
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:1
ENTER THE ELEMENT TO BE PUSHED INTO THE STACK:7
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:1
ENTER THE ELEMENT TO BE PUSHED INTO THE STACK:1
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:4
ELEMENTS OF STACK ARE:
5 7 1
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:3
ELEMENT AT TOP OF STACK IS 1
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:2
ELEMENT POPPED OUT IS 1
PRESS 1 TO CONTINUE 0 TO EXIT:1
1:PUSH 2:POP 3:PEEP 4:DISPLAY
ENTER WHICH STACK OPERATION TO PERFORM:4
ELEMENTS OF STACK ARE:
5 7
PRESS 1 TO CONTINUE 0 TO EXIT:0
PROGRAM FOR CREATING PACKAGES:
class Fibonacci:
	 def __init__(self,n):
		self.n=n
	 def fibo(self,n):
		 if n==1 or n==2:
			return 1
		 else:
			return((self.fibo(n-1)+self.fibo(n-2)))
		 def printfibo(self,n):
			 for i in range(1,(n+1)):
				print(self.fibo(i))
class Lucas:
	 def __init__(self,n):
		self.n=n
	 def luca(self,n) :
		if (n == 0) :
			return 2
		if (n == 1) :
			return 1
		return self.luca(n - 1) + self.luca(n - 2)
	 def printluca(self,n):
		for i in range(1,(n+1)):
			print(self.luca(i))

PACKAGE IMPORTED IN OTHER PROGRAM:
from series import Fibonacci
from series import Lucas
op=1
while(op!=3):
	 print("MENU\n1.FIBONACCI 2.LUCAS 3.EXIT")
	 op=int(input("ENTER YOUR OPTION:"))
	 if (op==1):
		 n=int(input("ENTER NUMBER OF TERMS: "))
		 obj=Fibonacci(n)
		 obj.printfibo(n)
	 elif (op==2):
		 n=int(input("ENTER NUMBER OF TERMS: "))
		 obj=Lucas(n)
		 obj.printluca(n)
	 else:
		break
OUTPUT:
MENU
1.FIBONACCI 2.LUCAS 3.EXIT
ENTER YOUR OPTION:1
ENTER NUMBER OF TERMS: 5
1
1
2
3
5
MENU
1.FIBONACCI 2.LUCAS 3.EXIT
ENTER YOUR OPTION:2
ENTER NUMBER OF TERMS: 5
1
3
4
7
11
MENU
1.FIBONACCI 2.LUCAS 3.EXIT
ENTER YPUR OPTION:3