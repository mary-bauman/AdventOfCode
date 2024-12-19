numLines = 10
arr = [input() for _ in range(numLines)]
regions = dict()
#regions[char] = [[(x,y) for xy in region]]
numRows = len(arr)
numCols = len(arr[0])
for r in range(numRows):
    for c in range(numCols):
        char = arr[r][c]
        if char not in regions:
            regions[char] = [[(r,c)]]
        else:
            #go through and make sure regions is combined
            #then look for region with neighbor for this
            #otherwise add this as a new region


# print(regions)


def shape_perimeter(points):
    perimeter = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for point in points:
        x, y = int(point[0]), int(point[1])
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in points:
                perimeter += 1
    return perimeter


total = 0
for char in regions:
    a = regions[char]
    for region in a:
        print(region)
        area = len(region)
        perimeter = shape_perimeter(region)
        print(f"Region {char}: Area = {area}, Perimeter = {perimeter}")
        total += area * perimeter


print(total)


