fin = open("5.inp", "r")
fout = open("5.out", "w")

inp = fin.readline()

alphaNum = [0] * 26

for i in inp:
    if i.islower() :
        alphaNum[ord(i) - ord('a')] += 1
    elif i.isupper() :
        alphaNum[ord(i) - ord('A')] += 1

char = [chr(x + ord('A')) for x in range(26)]
zipped = (list(zip(char, alphaNum)))

maximum = (max(zipped, key= lambda tup: tup[1]))

print (maximum[0], file = fout)

fout.close()
fin.close()
