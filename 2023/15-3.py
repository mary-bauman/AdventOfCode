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

# boxes = [([["",0]]*5)]*256
boxes = [[["", 0] for _ in range(5)] for _ in range(256)]
for b in range(len(a)):
    print(f"string = {a[b]} and box = {totals[b]}")
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

    inTheBox = False
    i = 0
    item = (boxes[totals[b]])[i]
    while (i < len((boxes[totals[b]]))-1 and item[0]==""):
        i+=1
        item = (boxes[totals[b]])[i]
    if(i == len((boxes[totals[b]]))-1):
        inTheBox = False
        i=0

    #print(f"boxes[totals[b]][i] = {boxes[totals[b]][i]}, inTheBox = {inTheBox}")
    print(f"box {totals[b]} = {(boxes[totals[b]])}")
    if(inTheBox):
        if(symbol=="="):
            boxes[totals[b]][i] = [title,number]
        else:
            boxes[totals[b]][i] = ("",0)
    else:
        if(symbol=="="):
            boxes[totals[b]][i] = [title,number]
        #else nothing happens
    #print(f"inTheBox = {inTheBox}")
    






            
print(f"boxes = {boxes}")



