with open("21input.txt") as f:
    NUM_LINES = 131
    line = f.readline()
    lineNum = 0
    garden = []
    start = set()
    while lineNum < NUM_LINES:
        garden.append(line)
        if 'S' in line:
            start.add((lineNum, line.index('S')))
        line = f.readline()
        lineNum += 1

NUM_STEPS = 64000
positions = start
memo = {}
gy = len(garden)
gx = len(garden[0])

for steps in range(0,NUM_STEPS):
    newPositions = set()
    for pos in positions:
        if pos in memo:
            newPositions.update(memo[pos])
        else:
            y, x = pos
            tempNewPositions = set()
            if garden[(y+1) % gy][x % gx] != '#':
                tempNewPositions.add((y+1, x))
            if garden[(y-1) % gy][x % gx] != '#':
                tempNewPositions.add((y-1, x))
            if garden[y % gy][(x+1) % gx] != '#':
                tempNewPositions.add((y, x+1))
            if garden[y % gy][(x-1) % gx] != '#':
                tempNewPositions.add((y, x-1))
            memo[pos] = tempNewPositions
            newPositions.update(tempNewPositions)
    positions = newPositions
print(len(positions))