import sys

userInp = sys.stdin.readlines()
splitted = [list(map(int, x.split())) for x in userInp]

print (splitted)

sums = []
leng = len(splitted)

# row
for x in splitted:
    sums.append(sum(x))

# col
for x in range(leng):
    s = 0
    for y in range(leng):
        s += splitted[y][x]
    sums.append(s)

# diagonal \
s = 0
for x in range(leng):
    s += splitted[x][x]
sums.append(s)

# diagonal /
s = 0
for x in range(leng):
    s += splitted[leng - x - 1][x]
sums.append(s)

print (sums)
print (max(sums))
