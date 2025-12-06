with open("in.txt") as f:
    a = []
    numRows = 4
    for _ in range(numRows):
        a.append(f.readline().strip().split())
    ops = f.readline().strip().split()
    numCols = len(a[0])

    total = 0
    for col in range(numCols):
        ans = 0
        op = ops[col]
        match op:
            case "+":
                for row in range(numRows):
                    ans += int(a[row][col])
            case "*":
                ans = 1
                for row in range(numRows):
                    ans *= int(a[row][col])

        total += ans
    
    print(total)