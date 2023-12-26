inputLen = 100
a = [""] * inputLen
rowLen = 0
for i in range(0,inputLen):
    a[i] = input()
    rowLen = len(a[i])

print(f"a = ")
for aa in range(inputLen):
    print(a[aa])

#pull all the rocks up
for currentCol in range(0,len(a[0])):
    currentRow = 0
    while(currentRow<inputLen and a[currentRow][currentCol]!="."):
        currentRow+=1
            #ok we should be on the lowest row thats an empty space 
    while(currentRow<inputLen):        
        #then we wanna find if theres an O and steal it
        row = currentRow + 1
        keepGoing = True
        if(a[currentRow][currentCol]!="."):
            keepGoing = False
        while (row < inputLen and keepGoing):
             if(a[row][currentCol]=="#"):
                  keepGoing = False
             elif(a[row][currentCol]=="O"):
                  tempS = a[currentRow][0:currentCol]
                  tempS += "O"
                  tempS += a[currentRow][currentCol+1:rowLen]
                  a[currentRow] = tempS
                  tempS = a[row][0:currentCol]
                  tempS += "."
                  tempS += a[row][currentCol+1:rowLen]
                  a[row] = tempS
                  row = inputLen
             row+=1
        currentRow+=1
for aa in range(inputLen):
    print(a[aa])

print(" ")
print("pull the rocks left now ")


for currentRow in range(0,len(a)):
    currentCol = 0
    while(currentCol<len(a[0]) and a[currentRow][currentCol]!="."):
        currentCol+=1
            #ok we should be on the lowest col thats an empty space 
    while(currentCol<len(a[0])):        
        #then we wanna find if theres an O and steal it
        col = currentCol + 1
        keepGoing = True
        if(a[currentRow][currentCol]!="."):
            keepGoing = False
        while (col < len(a[0]) and keepGoing):
             if(a[currentRow][col]=="#"):
                  keepGoing = False
             elif(a[currentRow][col]=="O"):
                  tempS = a[currentRow][:currentCol]
                  tempS += "O"
                  tempS += a[currentRow][currentCol+1:col]
                  tempS += "."
                  tempS += a[currentRow][col+1:]
                  a[currentRow] = tempS
                  col = len(a[0])
             col+=1
        currentCol+=1
for aa in range(len(a)):
    print(a[aa])







print(" ")
#count the rows
count = 0
for b in range(inputLen):
    rowCount = (inputLen-b)
    print(f"{a[b]}")
    for c in a[b]:
        if(c=="O"):
            count += rowCount

print(f"count = {count}")
#my answer = 111339
