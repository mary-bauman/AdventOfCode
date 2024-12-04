total = 0
numLines = 140
m = []
a = []
s = []
for i in range(numLines): 
    line = input()
    for j in range(len(line)):
        if line[j] == "M": m.append((i,j))
        elif line[j] == "A": a.append((i,j))
        elif line[j] == "S": s.append((i,j))
        
for x,y in a:
    #M.S
    #.A.
    #M.S
    if (x-1,y-1) in m and (x+1,y-1) in m and (x-1,y+1) in s and (x+1,y+1) in s: total += 1

    #S.M
    #.A.
    #S.M
    if (x-1,y-1) in s and (x+1,y-1) in s and (x-1,y+1) in m and (x+1,y+1) in m: total += 1
    
    #M.M
    #.A.
    #S.S
    if(x-1,y-1) in m and (x-1,y+1) in m and (x+1,y-1) in s and (x+1,y+1) in s: total += 1

    #S.S
    #.A.
    #M.M
    if(x-1,y-1) in s and (x-1,y+1) in s and (x+1,y-1) in m and (x+1,y+1) in m: total += 1

    
print(total)