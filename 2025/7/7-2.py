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

        cur.append(line)
        prev = prev2

    timelines = []
    newLine = []
    for c in cur[0]:
        if c=="S":
            newLine.append(1)
        else:
            newLine.append(0)
    timelines.append(newLine)
    timelines.append(newLine)

    for row in range(2, numLines):
        newLine = []
        line = cur[row]
        for col, c in enumerate(line):
            if col==0:
                if c=="." or c=="^": newLine.append(0)
                else: #c=="|"
                    numberOfTimelines = 0
                    if cur[row-1][col]=="|":
                        numberOfTimelines += timelines[row-1][col]
                    if cur[row][col+1]=="^":
                        numberOfTimelines += timelines[row-1][col+1]
                    newLine.append(numberOfTimelines)
            elif col==len(line)-1:
                if c=="." or c=="^": newLine.append(0)
                else: #c=="|"
                    numberOfTimelines = 0
                    if cur[row-1][col]=="|":
                        numberOfTimelines += timelines[row-1][col]
                    if cur[row][col-1]=="^":
                        numberOfTimelines += timelines[row-1][col-1]
                    newLine.append(numberOfTimelines)
            else:
                if c=="." or c=="^":
                    newLine.append(0)
                else: #c=="|"
                    numberOfTimelines = 0
                    if cur[row-1][col]=="|":
                        numberOfTimelines += timelines[row-1][col]
                    if cur[row][col-1]=="^":
                        numberOfTimelines += timelines[row-1][col-1]
                    if cur[row][col+1]=="^":
                        numberOfTimelines += timelines[row-1][col+1]
                    newLine.append(numberOfTimelines)
                
        timelines.append(newLine)
        
    print(sum(timelines[-1]))
