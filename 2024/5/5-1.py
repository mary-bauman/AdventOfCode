correct = []
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
    for i in range(len(vals)):
        for a,b in rules:
            if a==vals[i] and b in vals:
                if vals.index(b)<i:
                    good = False
            elif b==vals[i] and a in vals:
                if vals.index(a)>i:
                    good = False

    if good: correct.append(vals)
    



#find middle page numbers of each correct
# print(correct)
total = 0
for c in correct:
    if len(c)%2==1:
        total+=int(c[len(c)//2])
    else:
        print("why is this even")
print(total)