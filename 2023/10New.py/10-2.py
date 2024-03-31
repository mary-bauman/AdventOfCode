# https://adventofcode.com/2023/day/10#part2

# Placeholder for the code to be added

# Create an empty list to store the field
field = []

# Read the input file line by line and append each line to the field list
for y, line in enumerate(open(0)):
    field.append(line)
    
    # Find the starting position 'S' in the line and store its coordinates
    s_location = line.find('S')
    if s_location >= 0:
        x1, y1 = s_location, y

# Create a 2D list to mark the visited positions in the field
field_marked = [[False for i in range(len(field[0]))] for j in range(len(field))]

# Check if the starting position has a valid direction and set the start pipe accordingly
#I think the only reason we prioritize certain directions is soley to remove ambiguity
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

# Replace the starting position with the start pipe
field[y1] = field[y1][:x1] + start_pipe + field[y1][x1 + 1:]

# Save the current position
x, y = x1, y1

# Move through the field until reaching the starting position again
while True:
    # print(f"{x=}, {y=}, {direction=}")
    match direction:
        case "up":
            y -= 1
        case "right":
            x += 1
        case "down":
            y += 1
        case "left":
            x -= 1
    
    # Update the direction based on the current pipe
    match field[y][x]:
        case 'L':
            direction = "right" if direction == "down" else "up"
        case 'J':
            direction = "left" if direction == "down" else "up"
        case '7':
            direction = "down" if direction == "right" else "left"
        case 'F':
            direction = "down" if direction == "left" else "right"
    
    # Mark the current position as visited
    field_marked[y][x] = True
    
    # Break the loop if the starting position is reached again
    if x1 == x and y1 == y:
        break

total = 0

# Count the number of unmarked positions with odd number of connections

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

# Print the total count
print(total)