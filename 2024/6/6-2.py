

#note that memoization will speed this up if needed

def checkLoop(obstructionR, obstructionC,a,b,d,rows,cols,arr):
    newArr = arr.copy()
    newArr[obstructionR] = newArr[obstructionR][:obstructionC] + "#" + newArr[obstructionR][obstructionC+1:]
    # for a in newArr: print(a)
    # print()
    visited = []
    while [a,b,d] not in visited:
        if d=="up":
            if a==0: return False
            elif newArr[a-1][b]=='#': d = "right"
            else:
                visited.append([a,b,d])
                a-=1
        elif d=="right":
            if b==cols-1: return False
            elif newArr[a][b+1]=='#': d = "down"
            else:
                visited.append([a,b,d])
                b+=1
        elif d=="down":
            if a==rows-1: return False
            elif newArr[a+1][b]=='#': d = "left"
            else:
                visited.append([a,b,d])
                a+=1
        else:
            if b==0: return False
            elif newArr[a][b-1]=='#': d = "up"
            else:
                visited.append([a,b,d])
                b-=1
    return True

# lines=130
lines = 10
arr = []
for _ in range(lines): arr.append(input())
rows = lines
cols = len(arr[0])
a = 0
b = 0
d = "up"

for a2 in range(len(arr)):
    if '^' in arr[a2]:
        a = a2
        b = arr[a2].index('^')
        d = "up"
    elif '>' in arr[a2]:
        a = a2
        b = arr[a2].index('>')
        d = "right"
    elif 'v' in arr[a2]:
        a = a2
        b = arr[a2].index('v')
        d = "down"
    elif '<' in arr[a2]:
        a = a2
        b = arr[a2].index('<')
        d = "left"


total = 0
for r in range(rows):
    for c in range(cols):
        if arr[r][c]==".":
            if checkLoop(r,c,a,b,d,rows,cols,arr):
                # print("loop found at", r, c)
                total += 1
print(total)