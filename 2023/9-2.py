inputLen = 200
total = 0
def findDiffs(line):
    diffs = [0] * (len(line)-1)
    for a in range(1,(len(diffs))):
        diffs[a] = int(line[a+1])-int(line[a])
        if(int(line[a+1])<int(line[a])):
            print(f"int(line[a+1])-int(line[a]) = {int(line[a+1])-int(line[a])}")
    allDiffs.append(diffs)
    return diffs

for i in range(0,inputLen):
    allDiffs = []
    line = [0]
    line2 = (input().split(" "))
    for l in line2:
        line.append(l)
    #print(f"line = {line}")
    allDiffs.append(line)
    diffs = [0] * (len(line)-1)
    for a in range(1,(len(diffs))):
        diffs[a] = (int(line[a+1])-int(line[a]))
    print(f"diffs = {diffs}")
    allDiffs.append(diffs)
    zeros = all(x == 0 for x in diffs)

    while(not zeros):
        diffs = findDiffs(diffs)
        zeros = all(x == 0 for x in diffs)
    
    for d in range(len(allDiffs)-2,-1,-1):
        allDiffs[d][0] = int(allDiffs[d][1]) - int(allDiffs[d+1][0])
    print(allDiffs)
    total+=int(allDiffs[0][0])

print(f"total = {total}")
    