from collections import Counter
numLines = 1000
lefts = []
rights = []
for _ in range(numLines):
    line = input().split()
    lefts.append(int(line[0]))
    rights.append(int(line[1]))

total = 0
for l in lefts:
    if l in rights: total += (l * rights.count(l))

print(total)