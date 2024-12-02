def findSafe():
    level = [int(i) for i in input().split()]
    if level[1]>level[0]:
        #increasing
        for i in range(1, len(level)):
            diff = level[i]-level[i-1]
            if diff<1 or diff>3: return 0
    else:
        #decreasing
        for i in range(1, len(level)):
            diff = level[i-1] - level[i]
            if diff<1 or diff>3: return 0
    return 1

safe = 0
numLines = 1000
for _ in range(numLines):
    safe += findSafe()
    
print(safe)