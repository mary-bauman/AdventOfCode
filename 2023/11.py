inputLen = 140
allItems = [""] * (2 * inputLen)
allItemsi = 0


for i in range(0,inputLen):
    s = input()
    allItems[allItemsi] = s
    allItemsi+=1
    
    #expand the universe by adding row
    if(all(char == '.' for char in s)):
        allItems[allItemsi] = s
        allItemsi+=1


allItems = allItems[0:allItemsi]

#expand the universe by adding cols
b = 0
top = len(allItems[0])
while(b<top):
    s = [row[b] for row in allItems]
    if(all(char == '.' for char in s)):
        for i in range(allItemsi):
            a = allItems[i]
            st = str(a[0:b]) 
            st+= "." 
            st+= str(a[b:len(a)])
            allItems[i] = st
        b+=1
    b+=1

s = [row[b] for row in allItems]
if(all(char == '.' for char in s)):
    for i in range(allItemsi):
        a = allItems[i]
        st = str(a[0:b]) 
        st+= "." 
        st+= str(a[b:len(a)])
        allItems[i] = st

#print(f"allItems = {allItems}")
for i in allItems:
    print(i)

#ok at this point we have an array with the expanded universe




#add the coords of each galaxy
#assuming coors wont be too big here
coords = [[]] * (inputLen*10)
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

for c in range(len(coords)):
    pathTotals = []
    coord = coords[c]
    #print(f"galaxy = {c+1} = coord = {coord}")
    for a in range(c+1,len(coords)):
        #print(f"compare to galaxy = {a+1} = {coords[a]}")
        distanceX = abs(coord[0] - coords[a][0])
        distanceY = abs(coord[1] - coords[a][1])
        distance = distanceX + distanceY 
        #print(f"distance = {distanceX},{distanceY} = {distance}")
        pathTotals.append(distance)
    paths[c] = sum(pathTotals)








print(f"paths = {paths}")
print(f"sum = {sum(paths)}")
