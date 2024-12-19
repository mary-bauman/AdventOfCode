from math import ceil, inf
numLines = 4
options = [] 
tokens = 0
for _ in range(ceil(numLines/4)):
    input()
    b1 = (input()).split(": ")
    char1, x1, y1 = b1[0].split()[1], *map(int, [e.split("+")[1] for e in b1[1].split(", ")])
    b2 = (input()).split(": ")
    char2, x2, y2 = b2[0].split()[1], *map(int, [e.split("+")[1] for e in b2[1].split(", ")])
    prize = (input()).split(": ")[1].split(", ")
    prizeX = int(prize[0].split("=")[1])
    prizeY = int(prize[1].split("=")[1])
    options.append([char1, x1, y1, char2, x2, y2, prizeX, prizeY])


    # 3 tokens for A, 1 token for B
    # to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.
        

    if max(x1,x2)*100>=prizeX and max(y1,y2)*100>=prizeY:
        print(char1, x1, y1, char2, x2, y2, prizeX, prizeY)
        
        dp = [[inf] * (prizeX+1) for _ in range(prizeY+1)]
        dp[0][0] = 0
        dp[y1][x1] = 3
        dp[y2][x2] = 1
        for i in range(prizeY+1):
            for j in range(prizeX+1):
                if i>=y1 and j>=x1 and dp[i-y1][j-x1]>0:
                    dp[i][j] = dp[i-y1][j-x1]+3
                if i>=y2 and j>=x2 and dp[i-y2][j-x2]>0:
                    dp[i][j] = min(dp[i][j], dp[i-y2][j-x2]+1)

        # print("dp")
        # for d in dp: print(d)
        print("tokens = ", dp[prizeY][prizeX])
        if dp[prizeY][prizeX]<inf: tokens+=dp[prizeY][prizeX]
print(tokens)





