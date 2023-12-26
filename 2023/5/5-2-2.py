inputLen = 33
lineNum = 0
s = input().split(" ")
lineNum+=1
si = 1
seeds = []
while(si<len(s)):
    seedStart = int(s[si])
    seedEnd = int(s[si+1])
    seeds.append((seedStart,seedStart+seedEnd-1,False))
    si+=2
print(f"seeds = {seeds}")
seedsLen = len(seeds)
blankLine = input()
lineNum+=1

def round(seeds,lineNum):
