fin = open("2.inp", "r")
fout = open("2.out", "w")

first = int(fin.readline())
second = int(fin.readline())

add = first + second
sub = first - second
mul = first * second

minimum = min(add, min(sub, mul))
maximum = max(add, max(sub, mul))

print(minimum, file = fout)
print(maximum, file = fout)

fout.close()
fin.close()
