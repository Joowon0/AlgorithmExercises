inp = int(input())

stairNum = [1,2]

for x in range(2, inp):
    num = stairNum[-2] + stairNum[-1]
    stairNum.append(num)

print (stairNum[inp-1])
