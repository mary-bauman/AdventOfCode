inputLen = 200
total = 0
def findDiffs(line):
    diffs = [0] * (len(line)-1)
    for a in range(0,(len(diffs)-1)):
        diffs[a] = int(line[a+1])-int(line[a])
    allDiffs.append(diffs)
    return diffs

for i in range(0,inputLen):
    allDiffs = []
    line = input().split(" ")
    line.append("0")
    allDiffs.append(line)
    diffs = [0] * (len(line)-1)
    for a in range(0,(len(diffs)-1)):
        diffs[a] = int(line[a+1])-int(line[a])

    allDiffs.append(diffs)
    zeros = all(x == 0 for x in diffs)

    while(not zeros):
        diffs = findDiffs(diffs)
        zeros = all(x == 0 for x in diffs)
    
    for d in range(len(allDiffs)-2,-1,-1):
        allDiffs[d][-1] = int(allDiffs[d][-2]) + int(allDiffs[d+1][-1])
    print(allDiffs)
    total+=int(allDiffs[0][-1])

print(f"total = {total}")
    