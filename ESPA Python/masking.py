fin = open("4.inp", "r")
fout = open("4.out", "w")

inp = fin.readline()

for i in inp:
    if i.isdigit() :
        print ("*", file = fout, end = '')
    else:
        print (i, file = fout, end = '')

fout.close()
fin.close()
