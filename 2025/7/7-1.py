# numLines = 16
# with open("in-test.txt") as f:

numLines = 142
with open("in.txt") as f:

    def addPipe(line, prev2, pipeLocation, split):
        if pipeLocation>0: #left
            if line[pipeLocation-1]==".":
                line = line[:pipeLocation-1]+"|"+line[pipeLocation:]
                prev2.append(pipeLocation-1)
            elif line[pipeLocation-1]=="^":
                line, prev2, split = addPipe(line, prev2, pipeLocation-1, split + 1)

        if pipeLocation<len(line)-1: #right
            if line[pipeLocation+1]==".":
                line = line[:pipeLocation+1]+"|"+line[pipeLocation+2:]
                prev2.append(pipeLocation+1)
            elif line[pipeLocation+1]=="^":
                line, prev2, split = addPipe(line, prev2, pipeLocation+1, split + 1)

        return line, prev2, split


    cur = [f.readline().strip()]
    prev = [cur[0].index("S")]
    split = 0
    for _ in range (numLines-1) :
        line = f.readline().strip()
        prev2 = []
        for p in prev:
            if line[p]==".":
                line = line[:p]+"|"+line[p+1:]
                prev2.append(p)
            elif line[p]=="^":
                line, prev2, split = addPipe(line, prev2, p, split+1)   

        # print(f"line: {line}, prev2: {prev2}")  
        # print()
        cur.append(line)
        prev = prev2


    for c in cur: print("".join(c))
    print(split)
