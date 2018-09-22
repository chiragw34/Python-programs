import array
from array import *
a = array('i',[])
print("")
n = int(input("Enter the number of elements : "))
for i in range(n):
	a.append(int(input("Enter number %d : "%i)))
key =int(input("Enter the number to be searched :"))
found = a.index(key);
print("%d found at %d location"%(key,found+1))
