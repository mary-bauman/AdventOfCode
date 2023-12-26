instructions = input()
all = {}
alli = 0
programLen = 751
while(alli<programLen-1):
    i = str(input())
    key = i[0:3]
    left = i[7:10]
    right = i[12:15]
    all[key] = [left,right]
    alli+=1
print(all)

cur = "AAA"
curList = []
i = 0
count = 0
while(cur!="ZZZ"):
    count+=1
    curList.append(cur)
    if(i==len(instructions)):
        i = 0
    s = instructions[i]
    if(s=="L"):
        cur = all.get(cur)[0]
    elif(s=="R"):
        cur = all.get(cur)[1]
    else:
        print("wrong")
    i+=1
print(f"count = {count}")
#answer to part 1: 20221
#first guess to part 2: 25207 (too low)