def oneStep(garden, positions, steps):
    NUM_STEPS = 64
    if steps == NUM_STEPS:
        return len(positions)
    newPositions = set()
    for pos in positions:
        y, x = pos
        if y < len(garden) - 1:
            if garden[y+1][x] != '#':
                newPositions.add((y+1, x))
        if y > 0:
            if garden[y-1][x] != '#':
                newPositions.add((y-1, x))
        if x < len(garden[0]) - 1:
            if garden[y][x+1] != '#':
                newPositions.add((y, x+1))
        if x > 0:
            if garden[y][x-1] != '#':
                newPositions.add((y, x-1))
    return oneStep(garden, newPositions, steps+1)

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
    print(oneStep(garden, start, 0))
    