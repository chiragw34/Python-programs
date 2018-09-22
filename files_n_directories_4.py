import os
arr = next(os.walk('.'))[2]
print(arr)
str1=input()
x=os.path.isfile(str1)
if x:
     print("FILE",str1,"IS PRESENT")
else:
     print("FILE",str1,"IS NOT PRESENT")
