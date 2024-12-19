from collections import defaultdict

numLines = 50
arr = [input() for _ in range(numLines)]
numRows = numLines
numCols = len(arr[0])
positions = defaultdict(list)
antinodes = set()
for row in range(numRows):
    for col in range(numCols):
        c = arr[row][col]
        if c!='.':
            positions[c].append((row, col))
            antinodes.add((row, col))


for char in positions:
    n = len(positions[char])
    if n>1:
        for i in range(n):
            r,c = map(int, positions[char][i])
            for j in range(i+1, n):
                r2,c2 = map(int, positions[char][j])
                rDiff = r2-r
                cDiff = c2-c
                a1r = r - rDiff
                a1c = c - cDiff
                while a1c>=0 and a1r>=0 and a1c<numCols and a1r<numRows:
                    if arr[a1r][a1c]=='.':
                        antinodes.add((a1r, a1c))
                    a1r -= rDiff
                    a1c -= cDiff


                a2r = 2*r2-r
                a2c = 2*c2-c
                while a2c>=0 and a2r>=0 and a2c<numCols and a2r<numRows:
                    if arr[a2r][a2c]=='.':
                        antinodes.add((a2r, a2c))
                    a2r += rDiff
                    a2c += cDiff






# print(antinodes)
# for r,c in antinodes:
#     arr[r] = arr[r][:c]+'#'+arr[r][c+1:]
# for row in arr: print(row)
print(len(antinodes))