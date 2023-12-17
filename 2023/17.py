inputLen = 13
#inputLen = 141
heat = [[0 for _ in range(inputLen)] for _ in range(inputLen)]
for i in range(inputLen):
    heat[i] = [int(char) for char in input()]

print(f"lines = ")
for line in heat:
    print(line)

startRow = 0
startCol = 0
endRow = inputLen-1
endCol = inputLen-1
#so lets start at the end 
#and calculate the best way to get to the end from each posiiton
#(least heat damage)
#dp[element] = min heat damage to travel from element to end
dp = [[0 for _ in range(inputLen)] for _ in range(inputLen)]
#keeping a running count of what our last move was and how many times
lastMoves = [["",0]]
#at any point it can go up, down, left, right
#except the opposite of what it just did bc it cannot go backwards
#up means row--
#down means row++
#left means col--
#right means col++
#can eliminate moving options that are impossible bc of lastMoves and walls

#end from here is the interesting code 

def endFromHere(hereCol,hereRow):
    # endRow = inputLen-1
    # endCol = inputLen-1
    if(hereCol==endCol and hereRow==endRow):
        return heat[endRow][endCol]
    else:
        return 0
    







    
print("dp = ")
for d in range(len(dp)):
    for item in range(len(dp[d])):
        dp[d][item] = (endFromHere(d,item))
    print(dp[d])
