inputLen = 140
i = [""] * inputLen
for a in range(inputLen):
    i[a] = input()
total = 0

def findNums(rc):
    global total;
    newRc = []
    numbers = []
    for r in rc:
        row = r[0]
        col = r[1]
        left = col
        right = col
        if(col<len(i[row])-1):
            right +=1
        while(left>0 and i[row][left].isdigit() and ((row,left) not in newRc)):
            newRc.append((row,left))
            left-=1
        while(right<len(i[row]) and i[row][right].isdigit() and ((row,right) not in newRc)):
            newRc.append((row,right))
            right+=1
        if(right-left==1):
            num = 0
        else:
            num = str(i[row][left:right+1])
        
        numS = str(num).replace(".", "")
        numS = str(numS).replace("*", "")
        num = int(numS)

        numbers.append(num)
        #print(f"num = {num}")
        #print(f"left = {left}, right = {right}, num = {i[row][left+1:right]}")

    numbers = [value for value in numbers if value != 0]
    #print(f"numbers = {numbers}")
    if(len(numbers)==2):
        total+=(numbers[0] * numbers[1])


for b in range(inputLen):
    line = i[b]
    for ci in range(len(line)):
        curChar = i[b][ci]
        if(curChar=="*"):
            #gear found
            rowCols = []

            #check row above
            if (b>0):
                #check left digit
                if(ci>0):
                    if(i[b-1][ci-1].isdigit()):
                        rowCols.append(((b-1),(ci-1)))
                #right above it
                if(i[b-1][ci].isdigit()):
                    rowCols.append(((b-1),(ci)))
                #check right digit
                if(ci<inputLen-1):
                    if(i[b-1][ci+1].isdigit()):
                        rowCols.append(((b-1),(ci+1)))

            #check same row
            #check left digit
            if(ci>0):
                if(i[b][ci-1].isdigit()):
                    rowCols.append(((b),(ci-1)))
            #check right digit
            if(ci<inputLen-1):
                if(i[b][ci+1].isdigit()):
                    rowCols.append(((b),(ci+1)))
            #check row below
            if (b<inputLen-1):
                #check left digit
                if(ci>0):
                    if(i[b+1][ci-1].isdigit()):
                        rowCols.append(((b+1),(ci-1)))
                #right below it
                if(i[b+1][ci].isdigit()):
                    rowCols.append(((b+1),(ci)))
                #check right digit
                if(ci<inputLen-1):
                    if(i[b+1][ci+1].isdigit()):
                        rowCols.append(((b+1),(ci+1)))
            findNums(rowCols)
            


print(f"total = {total}")



