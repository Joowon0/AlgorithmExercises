inp = input()

inp = list(map(int, inp.split()))

print (inp)

fibo = [1, 1]
while inp[-1] > fibo[-1] :
    newNum = fibo[-2] + fibo[-1]
    fibo.append(newNum)
print (fibo)

flag = True
for x in inp:
    if x not in fibo :
        flag = False

if flag :
    print ('YES')
else :
    print ('NO')
