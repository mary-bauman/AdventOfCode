numLines1 = 8
numLines1 = 10
numLines1 = 50
totalLines = 10
totalLines = 21
totalLines = 71
numLines2 = totalLines - numLines1 - 1
arr = []
moves = []
for i in range(numLines1): arr.append(input())
input()
for i in range(numLines2):
    moveLine = input()
    for char in moveLine: moves.append(char)

# for a in arr: print(a)
# print()
# print(moves)

startR = 0
startC = 0
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == '@':
            startR = r
            startC = c
r,c = startR, startC

for m in moves:
    match m:
        case "^":
            if arr[r-1][c]=='.':
                arr[r] = arr[r][:c] + '.' + arr[r][c+1:]
                arr[r-1] = arr[r-1][:c] + '@' + arr[r-1][c+1:]
                r-=1
            elif arr[r-1][c]=='O':
                topR = r-1
                while arr[topR][c]=='O': topR -= 1
                if arr[topR][c]=='.':
                    arr[r] = arr[r][:c] + '.' + arr[r][c+1:]
                    arr[r-1] = arr[r-1][:c] + '@' + arr[r-1][c+1:]
                    for i in range(topR,r-1):
                        arr[i] = arr[i][:c] + "O" + arr[i][c+1:]
                    r-=1
                #else its a wall and we do nothing
            #else its a wall and we can just ignore this move
        case "v":
            if arr[r+1][c]=='.':
                arr[r] = arr[r][:c] + '.' + arr[r][c+1:]
                arr[r+1] = arr[r+1][:c] + '@' + arr[r+1][c+1:]
                r+=1
            elif arr[r+1][c]=='O':
                downR = r+1
                while arr[downR][c]=='O': downR += 1
                if arr[downR][c]=='.':
                    arr[r] = arr[r][:c] + '.' + arr[r][c+1:]
                    arr[r+1] = arr[r+1][:c] + '@' + arr[r+1][c+1:]
                    for i in range(r+2, downR+1):
                        arr[i] = arr[i][:c] + "O" + arr[i][c+1:]
                    r+=1
                #else its a wall and we do nothing
            #else its a wall and we can just ignore this move
        case "<":
            if arr[r][c-1]=='.':
                arr[r] = arr[r][:c-1] + "@." + arr[r][c+1:]
                c-=1
            elif arr[r][c-1]=='O':
                leftC = c-1
                while arr[r][leftC]=='O': leftC -= 1
                if arr[r][leftC]=='.':
                    arr[r] = arr[r][:leftC] + "O"*(c-leftC-1) + '@' + "." + arr[r][c+1:]
                    c-=1
                #else its a wall and we do nothing
            #else its a wall and we can just ignore this move
        case ">":
            if arr[r][c+1]=='.':
                arr[r] = arr[r][:c] + ".@" + arr[r][c+2:]
                c+=1
            elif arr[r][c+1]=='O':
                rightC = c+1
                while arr[r][rightC]=='O': rightC += 1
                # print("arr[r][rightC] = ", arr[r][rightC])
                if arr[r][rightC]=='.':
                    arr[r] = arr[r][:c] + "."+ "@" + "O"*(rightC-c-1) + arr[r][rightC+1:]
                    c+=1
                #else its a wall and we do nothing
            #else its a wall and we can just ignore this move
    # print()
    # print(m)
    # print(r,c)
    # for a in arr: print(a)

ans = 0
for a in arr: print(a)
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == 'O':
            ans += 100*r + c
print("ANS = ", ans)