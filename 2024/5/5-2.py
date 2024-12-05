incorrect = []
rules = []
line = input().split("|")
while line[0]!="change":
    rules.append(line)
    line = input().split("|")

# linesAfterChange = 6
linesAfterChange = 187
for _ in range(linesAfterChange):
    line = input()
    vals = line.split(",")
    good = True
    newVals = []
    for _ in range(100):
        for i in range(len(vals)):
            for a,b in rules:
                if a==vals[i] and b in vals:
                    if vals.index(b)<i:
                        vals[i],vals[vals.index(b)] = vals[vals.index(b)],vals[i]
                        good = False
                elif b==vals[i] and a in vals:
                    if vals.index(a)>i:
                        vals[i],vals[vals.index(a)] = vals[vals.index(a)],vals[i]
                        good = False
    

    if not good:
        #we gotta reorder vals
        # print(vals)
        incorrect.append(vals)
    



total = 0
for c in incorrect:
    if len(c)%2==1:
        total+=int(c[len(c)//2])
    else:
        print("why is this even")
print(total)