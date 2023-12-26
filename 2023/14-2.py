inputLen = 100
state = [""] * inputLen
rowLen = 0
for i in range(0,inputLen):
    state[i] = input()
    rowLen = len(state[i])

def goUp(state):
    #pull all the rocks up
    for currentCol in range(0,len(state[0])):
        currentRow = 0
        while(currentRow<len(state) and state[currentRow][currentCol]!="."):
            currentRow+=1
                #ok we should be on the lowest row thats an empty space 
        while(currentRow<len(state)):        
            #then we wanna find if theres an O and steal it
            row = currentRow + 1
            keepGoing = True
            if(state[currentRow][currentCol]!="."):
                keepGoing = False
            while (row < len(state) and keepGoing):
                if(state[row][currentCol]=="#"):
                    keepGoing = False
                elif(state[row][currentCol]=="O"):
                    tempS = state[currentRow][0:currentCol]
                    tempS += "O"
                    tempS += state[currentRow][currentCol+1:rowLen]
                    state[currentRow] = tempS
                    tempS = state[row][0:currentCol]
                    tempS += "."
                    tempS += state[row][currentCol+1:rowLen]
                    state[row] = tempS
                    row = len(state)
                row+=1
            currentRow+=1
    # print(f"\nup")
    # for s in state:
    #     print(s)
    return state

def goDown(state):
    for currentCol in range(0,len(state[0])):
        currentRow = len(state) - 1
        while(currentRow >= 0 and state[currentRow][currentCol]!="."):
            currentRow -= 1
        while(currentRow >= 0):        
            row = currentRow - 1
            keepGoing = True
            if(state[currentRow][currentCol]!="."):
                keepGoing = False
            while (row >= 0 and keepGoing):
                if(state[row][currentCol]=="#"):
                    keepGoing = False
                elif(state[row][currentCol]=="O"):
                    tempS = state[currentRow][0:currentCol]
                    tempS += "O"
                    tempS += state[currentRow][currentCol+1:rowLen]
                    state[currentRow] = tempS
                    tempS = state[row][0:currentCol]
                    tempS += "."
                    tempS += state[row][currentCol+1:rowLen]
                    state[row] = tempS
                    row = 0
                row-=1
            currentRow-=1
    # print(f"\ndown")
    # for s in state:
    #     print(s)
    return state

def goLeft(state):
    for currentRow in range(0,len(state)):
        currentCol = 0
        while(currentCol<len(state[0]) and state[currentRow][currentCol]!="."):
            currentCol+=1
                #ok we should be on the lowest col thats an empty space 
        while(currentCol<len(state[0])):        
            #then we wanna find if theres an O and steal it
            col = currentCol + 1
            keepGoing = True
            if(state[currentRow][currentCol]!="."):
                keepGoing = False
            while (col < len(state[0]) and keepGoing):
                if(state[currentRow][col]=="#"):
                    keepGoing = False
                elif(state[currentRow][col]=="O"):
                    tempS = state[currentRow][:currentCol]
                    tempS += "O"
                    tempS += state[currentRow][currentCol+1:col]
                    tempS += "."
                    tempS += state[currentRow][col+1:]
                    state[currentRow] = tempS
                    col = len(state[0])
                col+=1
            currentCol+=1
    # print(f"\nleft")
    # for s in state:
    #     print(s)
    return state

def goRight(state):
    for currentRow in range(0,len(state)):
        currentCol = len(state[0])-1
        while(currentCol >= 0 and state[currentRow][currentCol]!="."):
            currentCol-=1
                #ok we should be on the lowest col thats an empty space 
        while(currentCol >= 0):        
            #then we wanna find if theres an O and steal it
            col = currentCol - 1
            keepGoing = True
            if(state[currentRow][currentCol]!="."):
                keepGoing = False
            while (col >= 0 and keepGoing):
                if(state[currentRow][col]=="#"):
                    keepGoing = False
                elif(state[currentRow][col]=="O"):
                    tempS = state[currentRow][:col]
                    tempS += "."
                    tempS += state[currentRow][col+1:currentCol]
                    tempS += "O"
                    tempS += state[currentRow][currentCol+1:]
                    state[currentRow] = tempS
                    col = 0
                col-=1
            currentCol-=1
    # print(f"\nright")
    # for s in state:
    #     print(s)
    return state

memo = dict()
repeatedCycleNum = 0
for cycleNum in range(1_000_000_000):
    if tuple(state) in memo:
        repeatedCycleNum = memo[tuple(state)]
        break
    memo[tuple(state)] = cycleNum
    state = goUp(state)
    state = goLeft(state)
    state = goDown(state)
    state = goRight(state)
# print(cycleNum)
# print(repeatedCycleNum)

for _ in range((1_000_000_000 - repeatedCycleNum) % (cycleNum - repeatedCycleNum)):
    state = goUp(state)
    state = goLeft(state)
    state = goDown(state)
    state = goRight(state)
count = 0
for b in range(inputLen):
    rowCount = (inputLen-b)
    print(f"{state[b]}")
    for c in state[b]:
        if(c=="O"):
            count += rowCount

print(f"count = {count}")
#my answer to part 2 = 93736