numLines = 4493
with open("in.txt") as f:
    dial = 50
    pw = 0
    for _ in range (numLines) :
        line = f.readline().strip()
        i = int(line [1:])
        if line [0]=="L": i = (100-i)
        dial += i 
        dial %= 100
        if dial==0: pw+=1
    print (pw)