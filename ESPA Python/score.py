inp = input()

scores = []
if inp[0] == 'O':
    scores.append(1)
else:
    scores.append(0)

for i in inp[1:]:
    if i == 'X':
        scores.append(0)
    elif i == 'O':
        scores.append(scores[-1] + 1)

print (scores)
print (sum(scores))
