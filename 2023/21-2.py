import time
t1 = time.time()

positions = set()
with open("21input.txt") as f:
    NUM_LINES = 131
    line = f.readline()
    lineNum = 0
    garden = []
    while lineNum < NUM_LINES:
        garden.append(line)
        if 'S' in line:
            positions.add((lineNum, line.index('S')))
        line = f.readline()
        lineNum += 1

NUM_STEPS = 200
memo = {}
gy = len(garden)-1
gx = len(garden[0])

for steps in range(0,NUM_STEPS):
    newPositions = set()
    for pos in positions:
        if pos not in memo:
            y, x = pos
            tempNewPositions = {
                (y+1, x),
                (y-1, x),
                (y, x+1),
                (y, x-1)
            }
            memo[pos] = ((y,x) for (y,x) in tempNewPositions if garden[y%gy][x%gx] != '#')
        newPositions.update(memo[pos])
    positions = newPositions.copy()
    
print(len(positions))
print(f"time = {time.time()-t1}")