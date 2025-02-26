from math import inf


rows = 15
arr = [list(input()) for _ in range(rows)]
cols = len(arr[0])
# for a in arr: print(a)
startR = 0
startC = 0
endR = 0
endC = 0
for r in range(rows):
    for c in range(cols):
        if arr[r][c] == 'S':
            startR = r
            startC = c
        if arr[r][c] == 'E':
            endR = r
            endC = c

#. is track, # is wall





def findPathWithoutCheat(curR, curC, visited):
    if curR < 0 or curR >= rows or curC < 0 or curC >= cols or arr[curR][curC] == '#' or (curR, curC) in visited:
        return inf
    if curR == endR and curC == endC:
        return len(visited)
    visited.append((curR, curC))
    vis = findPathWithoutCheat(curR + 1, curC, visited)
    vis = min(vis, findPathWithoutCheat(curR - 1, curC, visited))
    vis = min(vis, findPathWithoutCheat(curR, curC + 1, visited))
    vis = min(vis, findPathWithoutCheat(curR, curC - 1, visited))
    return vis

#no cheat
#84 for test input
maxSeconds = findPathWithoutCheat(startR, startC, [])
print(maxSeconds)

doneVisited = []


def findPath(curR, curC, visited, cheatStart, cheatEnd):
    #start and end cheating are inclusive
    #if we're cheating than walls are fine
    if cheatStart <= len(visited) < cheatEnd:
        # print("We cheating at ", len(visited))
        # print("curR = ", curR)
        # print("curC = ", curC)
        # print(visited)
        # print()
        if curR < 0 or curR >= rows or curC < 0 or curC >= cols or (curR, curC) in visited:
            return 0
    elif curR < 0 or curR >= rows or curC < 0 or curC >= cols or arr[curR][curC] == '#' or (curR, curC) in visited:
        return 0
    if curR == endR and curC == endC:
        saved = maxSeconds - len(visited)
        #this is where we make sure its helpful enough
        if saved>0:
            if visited in doneVisited:
                return 0
            else:
                doneVisited.append(visited)
                print("saved = ", saved)
                print(visited)
                print("cheating at ", cheatStart, cheatEnd)
                print()
                return saved
        return 0
        
    visited.append((curR, curC))
    total = 0
    total += findPath(curR + 1, curC, visited, cheatStart, cheatEnd)
    total += findPath(curR - 1, curC, visited, cheatStart, cheatEnd)
    total += findPath(curR, curC + 1, visited, cheatStart, cheatEnd)
    total += findPath(curR, curC - 1, visited, cheatStart, cheatEnd)
    return total


ans = 0
#Each cheat has a distinct start position  and end position; 
#cheats are uniquely identified by their start position and end position.
#up to 2 picoseconds
for start in range(maxSeconds-2):
    saved1 = findPath(startR, startC, [], start, start+1)
    saved2 = findPath(startR, startC, [], start, start+2)
    # print("saved1 = ", saved1)
    # print("saved2 = ", saved2)
    ans += saved1
    ans += saved2

saved1 = findPath(startR, startC, [], maxSeconds-2, maxSeconds-1)
# print("saved1 = ", saved1)
ans += saved1
print("ans = ", ans)