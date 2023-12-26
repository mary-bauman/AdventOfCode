#inputLen = 237


#note:
#rewrite this so each block of code is a function that just gets called 6 times
#and also so seeds has (start,end,modifiedBoolean) so we can modify the same list the appropriate amount



inputLen = 33
lineNum = 0
s = input().split(" ")
lineNum+=1
si = 1
seeds = []
while(si<len(s)):
    seedStart = int(s[si])
    seedEnd = int(s[si+1])
    seeds.append((seedStart,seedStart+seedEnd-1))
    si+=2
print(f"seeds = {seeds}")
seedsLen = len(seeds)
blankLine = input()
lineNum+=1

seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = (sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            print("one")
            added = True
        elif(seedStart >= sourceStart and seedEnd >= sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            print("two")
            added = True
        elif(seedStart>=sourceStart and seedEnd>=sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
print(f"soil = {newSeeds}")
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"soil = {seeds}")



seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("soil to fert")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        # print(f"\nnew o = {o}")
        # print("newSeeds = " + str(newSeeds))
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        # print(f"source = {sourceStart,sourceEnd}")
        # print(f"seed = {seedStart,seedEnd}")
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedStart < sourceEnd and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  

seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"fert = {seeds}")


seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        print(f"\nnew o = {o}")
        print("newSeeds = " + str(newSeeds))
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        print(f"source = {sourceStart,sourceEnd}")
        print(f"seed = {seedStart,seedEnd}")
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"water = {seeds}")


seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"light = {seeds}")


seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"temp = {seeds}")


seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart < sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"humid = {seeds}")


seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("\n")
while(lineNum<inputLen-1):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
newSeeds = []
for si in range(0,len(seeds)):
    seedStart = int(seeds[si][0])
    seedEnd = int(seeds[si][1])
    added = False
    for o in options:
        if(added):
            break
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        sourceEnd = int(sourceStart+rangeLen-1)
        diff = int(destStart - sourceStart)
        #if seed start and end is before sourceStart then we do nothing
        #if seed start and end is after sourceEnd then we do nothing
        #if seed start and end is between source start and source end then we modidfy the whole range
        if(seedStart > sourceStart and seedEnd < sourceEnd):
            newSeeds.append(((seedStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart <= sourceStart and seedEnd >= sourceStart and seedEnd <= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append(((sourceStart+diff),(seedEnd + diff)))
            added = True
        elif(seedStart >= sourceStart and seedEnd > sourceEnd):
            newSeeds.append(((seedStart+diff),(sourceEnd+diff)))
            newSeeds.append(((sourceEnd),(seedEnd)))
            added = True
        elif(seedStart>sourceStart and seedEnd>sourceStart and seedEnd<= sourceEnd):
            newSeeds.append(((seedStart),(sourceStart-1)))
            newSeeds.append((sourceStart+diff,sourceEnd+diff))
            newSeeds.append(((sourceEnd+1),(seedEnd)))
            added = True   
    if(not added):
        newSeeds.append((seedStart,seedEnd))
        added = True  
seeds = sorted(newSeeds, key=lambda x: (x[0], x[1]))
#seeds = newSeeds
#condense seeds again to get rid of ranges that are contained in larger ranges?
seedsLen = len(seeds)
print(f"seeds = {seeds}")
m = min(s[0] for s in seeds)
print(f"min = {m}")
















