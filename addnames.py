givenStr = input()
calcStr1 = input()
calcStr2 = input()

givenStr = givenStr.split()
calcStr1 = calcStr1.split()
calcStr2 = calcStr2.split()

naturalNum = range(len(givenStr))
dic = dict(zip(givenStr, naturalNum))

calcNum1 = 0
calcNum2 = 0

for x in calcStr1:
    calcNum1 = calcNum1 * 10 + dic[x]
for x in calcStr2:
    calcNum2 = calcNum2 * 10 + dic[x]

print (dic)
print (calcNum1, calcNum2, calcNum1 + calcNum2)

switchedDict = {y:x for x,y in dic.items()}

print(switchedDict)

for x in str(calcNum1 + calcNum2):
    print (switchedDict[int(x)], end = ' ')
