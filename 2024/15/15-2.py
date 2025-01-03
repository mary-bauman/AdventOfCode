#to shift inputs to part two just double everything
#even @ has to be @.
totalLines = 9
gridLines = 7
grid = []
moves = []
for i in range(gridLines): grid.append(list(input()))
input()
for i in range(totalLines - gridLines-1):
    lineOfMoves = list(input())
    for move in lineOfMoves: moves.append(move)

r = 0
c = 0
for a in range(len(grid)):
    for b in range(len(grid[0])):
        if grid[a][b] == '@':
            r = a
            c = b




def goUp(r,c, involvedR, involvedC):
    print("GOING UP")
    





for m in moves:
    match m:
        case "^":
            if grid[r-1][c] == ".":
                grid[r-1][c] = "@"
                grid[r][c] = "."
                r -= 1
            else: goUp(r,c, [], [])
            
        case "v":
            if grid[r+1][c] == ".":
                grid[r+1][c] = "@"
                grid[r][c] = "."
                r += 1
        case "<":
            if grid[r][c-1] == ".":
                grid[r][c-1] = "@"
                grid[r][c] = "."
                c -= 1
            elif grid[r][c-1] == "]":
                newC = c-1
                while grid[r][newC] != ".":
                    newC-=1
                if grid[r][newC] == ".":
                    grid[r][c] = "."
                    grid[r][c-1] = "@"
                    for i in range(newC, c-2,2):
                        grid[r][i] = "["
                        grid[r][i+1] = "]"
                    c-=1
        case ">":
            if grid[r][c+1] == ".":
                grid[r][c+1] = "@"
                grid[r][c] = "."
                c += 1
            elif grid[r][c+1] == "[":
                newC = c+1
                while grid[r][newC] != ".":
                    newC+=1
                if grid[r][newC] == ".":
                    grid[r][c] = "."
                    grid[r][c+1] = "@"
                    for i in range(c+2, newC-1, 2):
                        grid[r][i] = "["
                        grid[r][i+1] = "]"
                    c+=1
    print()
    print(m)
    print(r,c)
    for g in grid: print("".join(g))
    print()


ans = 0
for g in grid: print("".join(g))
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            ans += 100*r + c
print("ANS = ", ans)