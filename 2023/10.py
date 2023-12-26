distancesFromS = []
inputLen = 5
all = [""] * (inputLen)
sLine = 0
allDistance = [[0] * (inputLen)] * (inputLen)

for i in range(inputLen):
    all[i] = input()
    if("S" in all[i]):
        sLine = i
print(f"all = {all}")

#ok lets find S in all

startingLine = all[sLine]
startingIndex = startingLine.index("S")
print(f"startingindex = {startingIndex}")


def move(x, y):
    s = all[y][x]
    print(f"s = {s}")
    if(s=="4"):
        allDistance[y][x] = 4
    




