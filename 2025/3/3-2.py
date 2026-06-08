from collections import Counter

def processLine (line):
    c = Counter(map (int, line) )
    n = len(line)
    ans = ""
    cur = 0
    for end in range (11,-1,-1): #forming num left to right
        highestNum = max(map (int, line[cur:n-end]) )
        ans+=str(highestNum)
        cur = line. index (str(highestNum), cur)+1
    return ans

ans = 0
numLines = 200
with open("in.txt") as f:
    for _ in range(numLines):
        line= f. readline().strip()
        lineSum = int(processLine (line))
        ans+=lineSum
print("ans = ", ans)