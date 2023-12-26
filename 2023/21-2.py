def oneStep(garden, positions, steps, memo):
    NUM_STEPS = 26501365
    if steps == NUM_STEPS:
        return len(positions)
    newPositions = set()
    for pos in positions:
        if pos in memo:
            print(pos)
            newPositions.update(memo[pos])
        else:
            y, x = pos
            tempNewPositions = set()
            if garden[(y+1) % len(garden)][x % len(garden[0])] != '#':
                newPositions.add((y+1, x))
                tempNewPositions.add((y+1, x))
            if garden[(y-1) % len(garden)][x % len(garden[0])] != '#':
                newPositions.add((y-1, x))
                tempNewPositions.add((y-1, x))
            if garden[y % len(garden)][(x+1) % len(garden[0])] != '#':
                newPositions.add((y, x+1))
                tempNewPositions.add((y, x+1))
            if garden[y % len(garden)][(x+1) % len(garden[0])] != '#':
                newPositions.add((y, x-1))
                tempNewPositions.add((y, x-1))
            memo[pos] = tempNewPositions
    return oneStep(garden, newPositions, steps+1, memo)

with open("input.txt") as f:
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
    print(oneStep(garden, start, 0, {}))