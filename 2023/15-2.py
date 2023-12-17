a = input().split(",")
totals = [0] * len(a)
for b in range(len(a)):
    val = 0
    letteri = 0
    while(letteri < len(a[b])):
        letter = a[b][letteri]
        if(letter=="=" or letter=="-"):
            letteri = len(a[b])+1
        else:
            ascii = ord(letter)
            val+= ascii
            val*=17
            val = val % 256
            letteri += 1
    totals[b] = val

print(f"{sum(totals)} totals = {totals}")

# boxes is a list of 256 ordered lists
# each element in ordered list is [key,number]
# we will manually loop through the list to search for the key
#lena is 4000

# boxes = [([["",0]]*3)]*256
boxes = [[["", 0] for _ in range(1000)] for _ in range(256)]
for b in range(len(a)):
    #print(f"string = {a[b]} and box = {totals[b]}")
    word = a[b]
    title = ""
    symbol = ""
    number = ""
    letterIndex = 0
    letter = word[letterIndex]
    while(letter!="=" and letter!="-"):
        title+=letter
        letterIndex+=1
        letter = word[letterIndex]
        symbol = str(letter)
    letterIndex+=1
    while(letterIndex<len(word)):
        letter = word[letterIndex]
        number+=str(letter)
        letterIndex+=1
    #print(f"{a[b]} title = {title}, symbol = {symbol}, number = {number}")
        

    #print(f"string is = {a[b]} and box = {totals[b]}")
    containedInBox = False
    containedIndex = 0
    for c in range(len(boxes[totals[b]])):
        #print(f"boxItem = {boxes[totals[b]][c]}")
        boxItem = boxes[totals[b]][c]
        if(boxItem[0]==title):
            containedInBox = True
            containedIndex = c
    
    #print(f"title {title} is contained in {boxes[totals[b]]} rn = {containedInBox}")

    if(symbol=="="):
        if(containedInBox):
            boxes[totals[b]][containedIndex][1] = int(number)
        else:
            c = 0
            while(c<len(boxes[totals[b]]) and boxes[totals[b]][c][0]!=''):
                c+=1
            #print(f"c={c}")
            if(c==len(boxes[totals[b]])):
               c = 0
            boxes[totals[b]][c] = [title,int(number)]
    else:
        if(containedInBox):
            boxes[totals[b]][containedIndex] = ["", 0]
            bottom = containedIndex
            top = (len(boxes[totals[b]]))-1
            while(bottom<top):
                boxes[totals[b]][bottom] = boxes[totals[b]][bottom+1]
                bottom+=1
            boxes[totals[b]][bottom] = ["", 0]

        #elses nothing happens

    print(f"boxes{[totals[b]]}= {boxes[totals[b]]}")




    


print(f"boxes = {boxes}")



boxTotals = [0] * len(boxes)
for i in range(len(boxes)):
    box = boxes[i]
    #print(f"box = {box}")
    for b in range(len(box)):
        item = box[b]
        #print(f"item = {item}")
        if(item[0]!=""):
            add = (i+1) * (b+1) * item[1]
            boxTotals[i] += add
            #print(f"add = {add}, i+1 = {i+1}, b+1 = {b+1}, item[1] = {item[1]}")
        


print(f"sum = {sum(boxTotals)}")
print(f"boxTotals = {boxTotals}")

#answer = 244342