print("APPEND FILE: ")
file=open("testfile.txt","a")
print("ENTER THE NO. OF LINES TO BE ENTERED: ")
n=input()
print("ENTER THE CONTENTS FOR FILE: ")
for i in range(int(n)):
     str=input()
     file.write(str+'\n')
file.close()
file=open("testfile.txt","r")
print("READING THE FILE")
print (file.read())
file.close()
