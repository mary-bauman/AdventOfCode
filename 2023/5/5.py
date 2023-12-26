#inputLen = 237
inputLen = 33
lineNum = 0
s = input().split(" ")
lineNum+=1
seeds = s
seeds = seeds[1:len(seeds)]
seedsLen = len(seeds)
seeds = [int(x) for x in seeds]
blankLine = input()
lineNum+=1
print(f"seeds1 = {seeds}")

seed_to_soil_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
print("seed to soil")
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,len(seeds)):
    seed = seeds[si]
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
    #print(f"seedValue = {seedValue}")
print(f"soil = {seeds}")


soil_to_fertilizer_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"fert = {seeds}")


fertilizer_to_water_map = input()
options = []
cur = input()
lineNum+=1
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"water = {seeds}")


water_to_light_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"light = {seeds}")


light_to_temp_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"temp = {seeds}")



temp_to_humid_map = input()
lineNum+=1
options = []
cur = input()
lineNum+=1
while(cur!=blankLine):
    options.append(cur.split(" "))
    cur = input()
    lineNum+=1
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"humid = {seeds}")


humid_to_location_map = input()
lineNum+=1
options = []
while(lineNum<inputLen-1):
    cur = input()
    lineNum+=1
    #print(cur)
    options.append(cur.split(" "))
for si in range(0,seedsLen):
    seed = int(seeds[si])
    seedValue = int(seed)
    for o in options:
        destStart = int(o[0])
        sourceStart = int(o[1])
        rangeLen = int(o[2])
        if(sourceStart<= seedValue and sourceStart+rangeLen>=seedValue):
            seeds[si] = int(destStart + (seedValue-sourceStart))
print(f"seeds8 = {seeds}")
print(f"min = {min(seeds)}")

#part 1: 251346198