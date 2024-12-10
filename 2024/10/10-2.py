numLines = 57
arr = [[(input())]for _ in range(numLines)]
for i in range(numLines):
    arr[i] = [int(c) for c in arr[i][0]]
numRows = len(arr)
numCols = len(arr[0])

def checkTrail(curR, curC, prevVal, numRows, numCols):
    if prevVal == 8 and arr[curR][curC] == 9: return 1
    if arr[curR][curC] != prevVal+1: return 0
    total = 0
    if curR>0:
        total+= checkTrail(curR-1, curC, arr[curR][curC], numRows, numCols)
    if curR < numRows-1:
        total+= checkTrail(curR+1, curC, arr[curR][curC], numRows, numCols)
    if curC > 0:
        total+= checkTrail(curR, curC-1, arr[curR][curC], numRows, numCols)
    if curC < numCols-1:
        total+= checkTrail(curR, curC+1, arr[curR][curC], numRows, numCols)
    return total

total = 0
for r  in range(numRows):
    for c in range(numCols):
        if arr[r][c] == 0:
            if r>0:  total+= checkTrail(r-1, c, 0, numRows, numCols)
            if r < numRows-1: total+= checkTrail(r+1, c, 0, numRows, numCols)
            if c>0: total+= checkTrail(r, c-1, 0, numRows, numCols)
            if c < numCols-1: total+= checkTrail(r, c+1, 0, numRows, numCols)
print(total)    

            
            