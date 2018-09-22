inp = int(input())

fibo = [1, 1]

while fibo[-1] < inp :
    newNum = fibo[-2] + fibo[-1]
    fibo.append(newNum)

print(fibo)

indexs = []
for x in range(len(fibo) - 1, 0, -1):
    if fibo[x] <= inp:
        indexs.append(x)
        inp -= fibo[x]
    print (x, fibo[x], indexs)


sorts = list(reversed(indexs))

print (sorts, inp)


for i in range(1, sorts[0]):
    print(0, end = '')
print(1, end = '')
for x in range( 1, len(sorts)):
    for i in range(1, sorts[x] - sorts[x-1]):
        print(0, end = '')
    print(1, end = '')
