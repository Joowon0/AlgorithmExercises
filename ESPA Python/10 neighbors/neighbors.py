import sys

def addZero(myList) :
    myList.insert(0, 0)
    myList.append(0)
    return myList
def dictReverse(myDict) :
    rev = {}
    for k, v in myDict.items():
        if v in rev :
            (x,y) = rev[v]
            if k[1] < y:
                rev[v] = k
            elif k[1] == y and k[0] < x:
                rev[v] = k
        else :
            rev[v] = k
    return rev

inp = sys.stdin.readlines()
splitted = [list(map(int, x.split())) for x in inp]

splitted.insert(0, [0] * len(splitted[0]))
splitted.append([0] * len(splitted[0]))
splitted = list((map(lambda x : addZero(x), splitted)))
print (splitted)

sums = {}
rowLen = len(splitted[0])
colLen = len(splitted)
for x in range (1, colLen - 1):
    for y in range(1, rowLen - 1):
        s = 0
        s += splitted[x-1][y-1]
        s += splitted[x-1][y]
        s += splitted[x-1][y+1]
        s += splitted[x][y-1]
        s += splitted[x][y+1]
        s += splitted[x+1][y-1]
        s += splitted[x+1][y]
        s += splitted[x+1][y+1]
        
        sums[(y, x)] = s

print (sums)
reversedSums = dictReverse(sums)

print(reversedSums)
(rstX, rstY) = reversedSums[max(reversedSums)]

print (rstX - 1, rstY - 1)
