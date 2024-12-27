numLines = 500
# numLines = 12
numRows = 103
# numRows = 7
numCols = 101
# numCols = 11
arr = [["." for _ in range(numCols)] for _ in range(numRows)]

#100 seconds grid
for _ in range(numLines):
    line = input().split()
    pos = line[0][2:].split(",")
    pc = int(pos[0])
    pr = int(pos[1])
    v = line[1][2:].split(",")
    vc = int(v[0])
    vr = int(v[1])
    c = (pc + 100*vc)%numCols
    r = (pr + 100*vr)%numRows
    if arr[r][c] == ".": arr[r][c] = "1"
    else: arr[r][c] = str(int(arr[r][c])+1)
# for a in arr: print(''.join(a))

#split into quadrants
q1sum = 0
q2sum = 0
q3sum = 0
q4sum = 0
q1 = []
for r in range(numRows//2):
    newR = []
    for c in range(numCols//2):
        if arr[r][c] != ".": q1sum += int(arr[r][c])
        newR.append(arr[r][c])
    q1.append(newR)
q2 = []
for r in range(numRows//2):
    newR = []
    for c in range(numCols//2+1, numCols):
        if arr[r][c] != ".": q2sum += int(arr[r][c])
        newR.append(arr[r][c])
    q2.append(newR)
q3 = []
for r in range(numRows//2+1, numRows):
    newR = []
    for c in range(numCols//2):
        if arr[r][c] != ".": q3sum += int(arr[r][c])
        newR.append(arr[r][c])
    q3.append(newR)
q4 = []
for r in range(numRows//2+1, numRows):
    newR = []
    for c in range(numCols//2+1, numCols):
        if arr[r][c] != ".": q4sum += int(arr[r][c])
        newR.append(arr[r][c])
    q4.append(newR)

# print("Q1", q1sum)
# for row in q1: print(''.join(row))
# print("Q2", q2sum)
# for row in q2: print(''.join(row))
# print("Q3", q3sum)
# for row in q3: print(''.join(row))
# print("Q4", q4sum)
# for row in q4: print(''.join(row))

ans = q1sum*q2sum*q3sum*q4sum
print(ans)