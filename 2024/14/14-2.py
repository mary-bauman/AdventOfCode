numLines = 500
numRows = 103
numCols = 101

lines = []
for _ in range(numLines):
    line = input().split()
    pos = line[0][2:].split(",")
    v = line[1][2:].split(",")
    lines.append([int(pos[0]), int(pos[1]), int(v[0]), int(v[1])])

for seconds in range(10000):
    arr = [["." for _ in range(numCols)] for _ in range(numRows)]
    for pc,pr,vc,vr in lines:
        c = (pc + seconds*vc)%numCols
        r = (pr + seconds*vr)%numRows
        if arr[r][c] == ".": arr[r][c] = "1"
        else: arr[r][c] = str(int(arr[r][c])+1)
    p = False
    for r in arr:
        if r.count('.')<numCols-30: p=True
    if p: 
        #this is for visually scanning for the tree
        print()
        print()
        print(seconds)
        print()
        print()
        print()
        for a in arr: print(''.join(a))

