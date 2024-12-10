numLines = 4
arr = [[(input())]for _ in range(numLines)]
for i in range(numLines):
    arr[i] = [int(c) for c in arr[i][0]]
# for a in arr: print(a)
numRows = len(arr)
numCols = len(arr[0])
dp = [[[] for _ in range(numCols)] for _ in range(numRows)]
for r in range(numRows):
    for c in range(numCols):
        if arr[r][c]==0:
            dp[r][c] = [0]


for r in range(numRows):
    for c in range(numCols):
        if arr[r][c] == 1:
            if r>0 and arr[r-1][c]==0: dp[r][c].append([r-1,c])
            if r<numRows-1 and arr[r+1][c]==0: dp[r][c].append([r+1,c])
            if c>0 and arr[r][c-1]==0: dp[r][c].append([r,c-1])
            if c<numCols-1 and arr[r][c+1]==0: dp[r][c].append([r,c+1])


for i in range(2,9):
    for r in range(numRows):
        for c in range(numCols):
            if arr[r][c] == i:
                if r>0 and arr[r-1][c]==i-1: dp[r][c] += dp[r-1][c]
                if r<numRows-1 and arr[r+1][c]==i-1: dp[r][c] += dp[r+1][c]
                if c>0 and arr[r][c-1]==i-1: dp[r][c] += dp[r][c-1]
                if c<numCols-1 and arr[r][c+1]==i-1: dp[r][c] += dp[r][c+1]

total = 0
for r in range(numRows):
    for c in range(numCols):
        if arr[r][c] == 9:
            ans = []
            if r>0 and arr[r-1][c]==8: ans += dp[r-1][c]
            if r<numRows-1 and arr[r+1][c]==8: ans += dp[r+1][c]
            if c>0 and arr[r][c-1]==8: ans += dp[r][c-1]
            if c<numCols-1 and arr[r][c+1]==8: ans += dp[r][c+1]
            unique = []
            for a in ans:
                if a not in unique: unique.append(a)
            ans = unique
            # print(ans)
            total += len(ans)

print(total)