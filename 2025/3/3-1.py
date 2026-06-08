from collections import Counter
def processLine (line):
    c = Counter(map (int, line) )
    highestNum = max(map (int, line) )

    #case 1: the highest num occurs multiple times like 909
    if c[highestNum] > 1: return (highestNum*10 + highestNum)

    idx = line.index(str(highestNum)) #bc now we know it only shows up once

    #case 2: the highest num is only somewhere other than the end like 900
    if idx < len(line)-1:
        return(highestNum*10 + max(map(int, line[idx+1:])))


    #case 3: the highest num is only at the end like 009 so we need next highest #find next lowest number that occurs
    ogHighestNum = highestNum
    highestNum -= 1
    while str(highestNum) not in line: highestNum -= 1

    return (highestNum*10 + ogHighestNum)

ans = 0
numLines= 200
with open("in.txt") as f:
    for _ in range (numLines):
        line= f. readline().strip()
        lineSum = processLine (line)
        ans+=lineSum
print("ans =", ans)