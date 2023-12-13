inputLen = 10
allItems = [""] * (2 * inputLen)
allItemsi = 0

colsExpanded = []
rowsExpanded = []

for i in range(0,inputLen):
    s = input()
    allItems[allItemsi] = s
    allItemsi+=1
    #expand the universe by adding row
    if(all((char == '.' or char == '@') for char in s)):
        allItems[allItemsi] = "@" * (len(s))
        rowsExpanded.append(allItemsi)
        allItemsi+=1
        


allItems = allItems[0:allItemsi]

#expand the universe by adding cols
b = 0
top = len(allItems[0])
while(b<top):
    s = [row[b] for row in allItems]
    #print(f"b = {b} and s = {s}")
    if(all((char == '.' or char == '@') for char in s)):
        #print(f"add col at {allItemsi}")
        for i in range(allItemsi):
            a = allItems[i]
            st = str(a[0:b]) 
            st+= "@" 
            st+= str(a[b:len(a)])
            allItems[i] = st
        colsExpanded.append(b)
        b+=1
        top+=1
    b+=1

#print(f"allItems = {allItems}")
for i in allItems:
    print(i)

#ok at this point we have an array with the expanded universe




#add the coords of each galaxy
#assuming coors wont be too big here
coords = [[]] * (inputLen*1000)
coordsi = 0

for si in range(len(allItems)):
    s = allItems[si]
    for c in range(0,len(s)):
        if(s[c]=="#"):
            coords[coordsi] = [si,c]
            coordsi+=1
            #print(f"coords = {coords}")
            #print(f"coordsi = {coordsi}")
          
coords = coords[0:coordsi]
print(f"coords = {coords}")

#shortest paths between each galaxy 
#start with the first galaxy and find the distance to all galaxies after i
#paths is the sum of each galaxy and the distances of galaxies after it
#path totals is the sum for each distance from that specific galaxy
paths = [0] * len(coords)


print(f"colsExpanded = {colsExpanded}")
print(f"rowsExpanded = {rowsExpanded}")

for c in range(len(coords)):
    pathTotals = []
    coord = coords[c]
    print(f"galaxy = {c+1} = coord = {coord}")
    for a in range(c+1,len(coords)):
        print(f"compare to galaxy = {a+1} = {coords[a]}")
        rowDistance = 0
        colDistance = 0
        rowStart = min(coord[0],coords[a][0])
        rowEnd = max(coord[0],coords[a][0])
        colStart = min(coord[1],coords[a][1])
        colEnd = max(coord[1],coords[a][1])
        while(rowStart<rowEnd):
            #print(f"rowStart = {rowStart} and rowEnd = {rowEnd}")
            if(allItems[rowStart][0:4]=="@@@@"):
                rowDistance += 10
            else:    
                rowDistance += 1
            rowStart+=1
        while(colStart<colEnd):
            if(allItems[0][colStart]=="@" and allItems[1][colStart]=="@" and allItems[2][colStart]=="@"):
                colDistance += 10
            else:
                colDistance += 1
            colStart+=1
        distance = rowDistance + colDistance
        print(f"distance = {rowDistance},{colDistance} = {distance}")
        pathTotals.append(distance)
    paths[c] = sum(pathTotals)
        


# for c in range(len(coords)):
#     pathTotals = []
#     coord = coords[c]
#     print(f"galaxy = {c+1} = coord = {coord}")
#     for a in range(c+1,len(coords)):
#         print(f"compare to galaxy = {a+1} = {coords[a]}")
#         distanceRow = abs(coord[0] - coords[a][0])
#         bigger = int(coord[0])
#         smaller = int(coords[a][0])
#         if(coord[0]<coords[a][0]):
#             bigger = int(coords[a][0])
#             smaller = int(coord[0])
#         #print(f"bigger = {bigger}")
#         #print(f"smaller = {smaller}")
        
#         for colNumber in range (0,len(colsExpanded)):
#             col = colsExpanded[colNumber]
#             #print(f"colNumber = {col}, smaller = {smaller}, bigger = {bigger}")
#             if(col>smaller and col<bigger):
#                 #print(f"distanceX += 1000000")
#                 distanceRow += 1000000-1


#         distanceCol = abs(coord[1] - coords[a][1])

#         bigger = int(coord[1])
#         smaller = int(coords[a][1])
#         if(coord[0]<coords[a][1]):
#             bigger = int(coords[a][1])
#             smaller = int(coord[1])
#         #print(f"bigger = {bigger}")
#         #print(f"smaller = {smaller}")
        
#         for rowNumber in range (0,len(rowsExpanded)):
#             row = rowsExpanded[rowNumber]
#             if(row>smaller and row<bigger):
#                 distanceCol += 1000000-1



#         distance = distanceRow + distanceCol
#         print(f"distance = {distanceRow},{distanceCol} = {distance}")
#         pathTotals.append(distance)
#     paths[c] = sum(pathTotals)

xxx = []
x =  [0, 15, 15, 27, 27, 42, 42, 42, 30],[0, 28, 14, 40, 27, 42, 55, 41],[0, 38, 14, 53, 53, 27, 41],[26, 15, 39, 41, 27],[0, 27, 15, 41, 27],[0, 24, 52, 38],[0, 28, 14],[0, 14]
for xx in x:
    print(sum(xx))
    xxx.append(sum(xx))
print(sum(xxx))

print(f"paths = {paths}")
print(f"sum = {sum(paths)}")


#first submission: 9076510 (too low)
#attempt 2: 15085061434 (too low)
#attempt 3: 15085387950 (too low)
#attempt 4: 216763186272 (wrong)
