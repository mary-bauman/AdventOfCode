numLines = 39
numLines = 3999
locks = []
keys = []
curArr = []
#lock = False means its a key
lock = True
for _ in range(numLines):
    if curArr == []:
        firstLine = input()
        if firstLine == "#####":
            lock = True
            curArr.append(firstLine)
        else:
            lock = False
            curArr.append(firstLine)
    else:
        line = input()
        if len(line) == 5: curArr.append(line)
        else:
            if lock: locks.append(curArr)
            else: keys.append(curArr)
            curArr = []
if lock: locks.append(curArr)
else: keys.append(curArr)
curArr = []


#use the locks # starting from the top
#use the keys . starting from the top
#for a key to fit in the lock, each key col must be the same or more than lock col

keyNums = []
for key in keys:
    col0 = 0
    col1 = 0
    col2 = 0
    col3 = 0
    col4 = 0
    while key[col0][0] == "." and col0 < 5:
        col0 += 1
    if key[col0][0] == "#": col0-=1
    while key[col1][1] == "." and col1 < 5:
        col1 += 1
    if key[col1][1] == "#": col1-=1
    while key[col2][2] == "." and col2 < 5:
        col2 += 1
    if key[col2][2] == "#": col2-=1
    while key[col3][3] == "." and col3 < 5:
        col3 += 1
    if key[col3][3] == "#": col3-=1
    while key[col4][4] == "." and col4 < 5:
        col4 += 1
    if key[col4][4] == "#": col4-=1
    keyNums.append([col0, col1, col2, col3, col4])
keys = keyNums

lockNums = []
for lock in locks:
    col0 = 0
    col1 = 0
    col2 = 0
    col3 = 0
    col4 = 0
    while lock[col0+1][0] == "#" and col0 < 5:
        col0 += 1
    if lock[col0][0] == ".": col0-=1
    while lock[col1+1][1] == "#" and col1 < 5:
        col1 += 1
    if lock[col1][1] == ".": col1-=1
    while lock[col2+1][2] == "#" and col2 < 5:
        col2 += 1
    if lock[col2][2] == ".": col2-=1
    while lock[col3+1][3] == "#" and col3 < 5:
        col3 += 1
    if lock[col3][3] == ".": col3-=1
    while lock[col4+1][4] == "#" and col4 < 5:
        col4 += 1
    if lock[col4][4] == ".": col4-=1
    lockNums.append([col0, col1, col2, col3, col4])
locks = lockNums


#finding unique key and lock pairs
ans = 0
for l0,l1,l2,l3,l4 in locks:
    for k0,k1,k2,k3,k4 in keys:
        if k0 >= l0 and k1 >= l1 and k2 >= l2 and k3 >= l3 and k4 >= l4:
            ans +=1
    
print("ans = ", ans)
