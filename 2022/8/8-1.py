with open("in-test.txt") as f:
    numLines = 5
    grid = []
    for _ in range(numLines):
        grid.append(list(f.readline().strip()))
    
    for g in grid: print(g)
    print()

    #so the current issues is that sight can turn conrners
    #so direction matters here only one direction allowed.
    #each cell can know the tallest tower blocking from each of the four directiosn

    rows = numLines
    cols = len(grid[0])
    ans = rows*2 + cols*2 - 4
    # for r in range(1, rows-1):
    #     for c in range(1, rows-1):
    #         val = grid[r][c]

    #block contains the shortest tower that blocks view
    block = []
    block.append(grid[0].copy())
    for g in grid[1:rows-1]:
        block.append([g[0]] + ['0']*(cols-2) + [g[cols-1]])
    block.append(grid[-1].copy())

    # for b in block: print(b)
    # print()

    #left to right
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            block[r][c] = max(block[r][c], block[r][c-1], grid[r][c-1])
    
    # for b in block: print(b)

    #right to left
    for r in range(1,rows-1):
        for c in range(cols-2,0,-1):
            block[r][c] = min((max(block[r][c+1], grid[r][c+1])), block[r][c])
            
    # for b in block: print(b)
    # print()

    #top to bottom
    for c in range(1,cols-1):
        for r in range(1,rows-1):
            block[r][c] = min((max(block[r-1][c], grid[r-1][c])), block[r][c])

    # for b in block: print(b)
    # print()

    #bottom to top
    for c in range(1,cols-1):
        for r in range(rows-2,0,-1):
            block[r][c] = min((max(block[r+1][c], grid[r+1][c])), block[r][c])

    
    for b in block: print(b)
    print()

    ans = rows*2 + cols*2 - 4
    print(ans)
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            ans += int(grid[r][c] > block[r][c])

    print(ans)


        

    
      
    
        
    
