instructions = input()
allDict = {}
alli = 0
programLen = 751
curs = []
#throw allDict the input lines into a dictionary called allDict
while(alli<programLen-1):
    i = str(input())
    key = i[0:3]
    left = i[7:10]
    right = i[12:15]
    allDict[key] = [left,right]
    if(key[2]=="A"):
        curs.append(key)
    alli+=1
#allDict is a dict with allDict possible moves
#curs is a list with allDict the nodes on each step
print(allDict)
print(f"curs = {curs}")

i = 0
count = 0
done = False

while(not done):
    count+=1
    d = 0 if instructions[i] == "L" else 1
    curs = [allDict.get(c)[d] for c in curs]
    done = all(item.endswith("Z") for item in curs)
    i = (i + 1) % len(instructions)

print(f"count = {count}")

#first guess to part 2: 25207 (too low)