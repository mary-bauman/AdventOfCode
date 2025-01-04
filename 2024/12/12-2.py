from collections import defaultdict


rows = 10
rows = 140
arr = [list(input()) for _ in range(rows)]
cols = len(arr[0])
for a in arr: print(a)

def area(region):
    return len(region)

def perimeter(region):
    #above[r] contains c which have an edge above them
    above = defaultdict(list)
    below = defaultdict(list)
    #left[c] contains r which have an edge to the left of them
    left = defaultdict(list)
    right = defaultdict(list)
    sides = 0

    for r,c in region:
        if (r-1,c) not in region:
            above[r].append(c)
        if (r+1,c) not in region:
            below[r].append(c)
        if (r,c-1) not in region:
            left[c].append(r)
        if (r,c+1) not in region:
            right[c].append(r)

    for r in above:
        cs = above[r]
        cs = [int(c) for c in cs]
        cs.sort()
        groups = 1
        for i in range(1,len(cs)):
            if cs[i]-cs[i-1]>1:
                groups += 1
        sides += groups

    for r in below:
        cs = below[r]
        cs = [int(c) for c in cs]
        cs.sort()
        groups = 1
        for i in range(1,len(cs)):
            if cs[i]-cs[i-1]>1:
                groups += 1
        sides += groups
    
    for c in left:
        rs = left[c]
        rs = [int(r) for r in rs]
        rs.sort()
        groups = 1
        for i in range(1,len(rs)):
            if rs[i]-rs[i-1]>1:
                groups += 1
        sides += groups
    
    for c in right:
        rs = right[c]
        rs = [int(r) for r in rs]
        rs.sort()
        groups = 1
        for i in range(1,len(rs)):
            if rs[i]-rs[i-1]>1:
                groups += 1
        sides += groups

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

