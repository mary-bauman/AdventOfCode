rows = 10
rows = 140
arr = [list(input()) for _ in range(rows)]
cols = len(arr[0])
for a in arr: print(a)

def area(region):
    return len(region)

def perimeter(region):
    sides = 0
    for r,c in region:
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            if (r+dr,c+dc) not in region:
                sides += 1
    return sides



ans = 0
done = set()
for r in range(rows):
    for c in range(cols):
        if (r,c) not in done:
            region = []
            stack = [(r,c)]
            char = arr[r][c]
            while stack:
                x,y = stack.pop()
                # print("x = ", x, "y = ", y)
                if arr[x][y]==char and (x,y) not in done:
                    done.add((x,y))
                    region.append((x,y))
                    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                        if x+dx>=0 and x+dx<rows and y+dy>=0 and y+dy<cols:
                            stack.append((x+dx,y+dy))


            # print(f"region for {char} = ")
            # for reg in region: print(reg)
            total = area(region)
            p = perimeter(region)
            print("area = ", total, "perimeter = ", p)
            total *= p
            ans += total
            done.add((r,c))
        # print("c = ", c)

print("ans = ", ans)

