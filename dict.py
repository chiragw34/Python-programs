mydict1={'name':input("enter the name:"),'age':int(input("enter the age:")),'marks':int(input("enter the marks:"))}
print(mydict1)
mydict1['name']=input("enter the name to be updated:")
print("updation succesfull!")
print(mydict1)
if (input("enter a key to be searched:") in mydict1):
    print("key is present")
else:
    print("key is not present")
del mydict1[input("enter what you want to delete:")]
print("deletion succesfull")
print(mydict1)
