fin = open("3.inp", "r")
fout = open("3.out", "w")

first = fin.readline()
second = fin.readline()

alphaNum = [0] * 26

for i in first[:-1]:    
    alphaNum[ord(i) - ord('a')] += 1

for i in second[:-1]:
    alphaNum[ord(i) - ord('a')] -= 1

flag = True
for i in alphaNum:
    if (i != 0):
        flag = False

if (flag) :
    print ("YES", file = fout)
else :
    print ("NO", file = fout)


fout.close()
fin.close()
