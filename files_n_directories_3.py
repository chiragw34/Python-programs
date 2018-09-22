f = open("testfile.txt", "r")
c=0
c1=0
c2=0
for line in f:
    count = line.split()
    c += 1
    c1+=len(count)
    for j in line:
        c2+=1
print("THE NO. OF LINES IN TESTFILE ARE: %d"%c)
print("THE NO. OF WORDS IN TESTFILE ARE: %d"%c1)
print("THE NO. OF CHARACTERS IN TESTFILE ARE: %d"%c2)
