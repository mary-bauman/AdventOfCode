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
counts = [0] * len(curs)
instruct = len(instructions)
for c in range(0,6):
    cur = curs[c]
    while(str(curs[c][2])!="Z"):
        counts[c]+=1
        d = 0 if instructions[i] == "L" else 1
        curs[c] = allDict.get(curs[c])[d]
        i = (i + 1) % instruct




print(f"counts = {counts}")
lcm = 1
from math import gcd
for c in counts:
    lcm = lcm*c//gcd(lcm, c)
print(lcm)

