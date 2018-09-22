a = []
a = input("Enter the array A:").split(" ")
print(a)
b = input("Enter the number B:").split(" ")
n = len(a)
ans = []
for i in a:
    if float(i) is 1:
        continue
    if float(i) is 0:
        continue
    if (float(i) > float(b)):
        continue
    #print(b%int(i))
    if (float(b)%float(i) is 0):
        ans.append(float(i))
print(len(ans))
