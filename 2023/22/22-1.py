inputLen = 7
blocks = []
for i in range(inputLen):
    line = input().split("~")
    line1 = line[0].split(",")
    line2 = line[1].split(",")
    xLow = min(line1[0], line2[0])
    xHigh = max(line1[0], line2[0])
    yLow = min(line1[1], line2[1])
    yHigh = max(line1[1], line2[1])
    zLow = min(line1[2], line2[2])
    zHigh = max(line1[2], line2[2])
    blocks.append((xLow,xHigh,yLow,yHigh,int(zLow),zHigh))

#go bottom up from zL
blocks = sorted(blocks, key=lambda x: int(x[4]))  
for b in blocks:
    print (b)


#each block falls down and goes into newBlocks
newBlocks = []
for (xL, xH, yL, yH, zL, zH) in blocks:
    #1 is the lowest a block can be
    clearPath = True
    while(zL>1 and clearPath):
        #if there is a block in the way below, 
            #fall until we hit that block
        clearPath = False

        #else fall until zL = 1

