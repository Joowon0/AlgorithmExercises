inp = int(input())

persons = list(range(inp))
print(persons)

killIdx = 1
while len(persons) > 1:
    del persons[killIdx]
    killIdx += 1
    killIdx %= len(persons)


print (persons[0] + 1)
