def checkSafe(levels):
    if not levels: return True
    if all(((levels[i]-levels[i+1])>=1 and (levels[i]-levels[i+1])<=3)  for i in range(len(levels)-1)): return True
    if all(((levels[i+1]-levels[i])>=1 and (levels[i+1]-levels[i])<=3) for i in range(len(levels)-1)): return True
    return False

numLevels = 1000
safe = 0
for _ in range(numLevels):
    levels = [int(i) for i in input().split()]
    if checkSafe(levels): safe+=1
    else:
        for i in range(len(levels)):
            if checkSafe(levels[:i]+levels[i+1:]):
                safe+=1
                break

print(safe)