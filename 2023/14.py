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
        #print(f"currentRow = {currentRow}")
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
        # print(f"currentRow = {currentRow} ")
        # for aa in range(inputLen):
        #     print(a[aa])
            
        currentRow+=1

#answer = 111339
    




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

