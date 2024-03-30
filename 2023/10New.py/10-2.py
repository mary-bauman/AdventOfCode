# https://adventofcode.com/2023/day/10#part2

field = []
for y, line in enumerate(open(0)):
    field.append(line)
    s_location = line.find('S')
    if s_location >= 0:
        x1, y1 = s_location, y
field_marked = [[False for i in range(len(field[0]))] for j in range(len(field))]
if y1 > 0 and field[y1 - 1][x1] in {'7', 'F', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = "up"
        start_pipe = 'J'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = "up"
        start_pipe = 'L'
if y1 < len(field) - 1 and field[y1 + 1][x1] in {'J', 'L', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = "down"
        start_pipe = '7'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = "down"
        start_pipe = 'F'
if 0 < x1 < len(field[0]) - 1 and field[y1][x1 - 1] in {'F', 'L', '-'} and field[y1][x1 + 1] in {'7', 'J', '-'}:
    direction = "right"
    start_pipe = '-'
if 0 < y1 < len(field) - 1 and field[y1 - 1][x1] in {'F', '7', '|'} and field[y1 + 1][x1] in {'L', 'J', '|'}:
    direction = "up"
    start_pipe = '|'
field[y1] = field[y1][:x1] + start_pipe + field[y1][x1 + 1:]
x, y = x1, y1
while True:
    match direction:
        case "up":
            y -= 1
        case "right":
            x += 1
        case "down":
            y += 1
        case "left":
            x -= 1
    match field[y][x]:
        case 'L':
            direction = "right" if direction == "down" else "up"
        case 'J':
            direction = "left" if direction == "down" else "up"
        case '7':
            direction = "down" if direction == "right" else "left"
        case 'F':
            direction = "down" if direction == "left" else "right"
    field_marked[y][x] = True
    if x1 == x and y1 == y:
        break
total = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if not field_marked[y][x]:
            n = 0
            for y1 in range(y + 1, len(field)):
                if field_marked[y1][x]:
                    if field[y1][x] == '-':
                        n += 1
                    elif field[y1][x] == '7' or field[y1][x] == 'F':
                        prev = field[y1][x]
                    elif (field[y1][x] == 'J' and prev == 'F') or (field[y1][x] == 'L' and prev == '7'):
                        n += 1
            if n % 2 == 1:
                total += 1
print(total)