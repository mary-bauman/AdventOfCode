numLines = 1000
lefts = []
rights = []
for _ in range(numLines):
    line = input().split()
    lefts.append(int(line[0]))
    rights.append(int(line[1]))

distance = 0
lefts.sort()
rights.sort()
for i in range(numLines):
    distance += abs(rights[i] - lefts[i])

print(distance)