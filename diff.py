fin = open("1.inp", "r")
fout = open("1.out", "w")

a = int(fin.readline())
b = int(fin.readline())

print >> fout, max(a,b) - min(a,b)

fout.close()
fin.close()
