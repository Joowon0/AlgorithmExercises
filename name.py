numberingStr = input()
calcStr = input()

splittedStr = numberingStr.split()
naturalNum = range(len(splittedStr))
numbering = dict(zip(splittedStr, naturalNum))

splittedCalcStr = calcStr.split()
calcNum = 0
for x in splittedCalcStr:
    calcNum = calcNum * 10 + numbering[x]

print (calcNum)
print (calcNum ** 2)
