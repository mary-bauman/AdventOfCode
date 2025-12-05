# freshLines = 4
# availableLines = 6
freshLines = 169
availableLines = 1170-1-freshLines
fresh = []
available = []
# with open("in-test.txt") as f:
with open("in.txt") as f:
    for _ in range(freshLines):
        line = f.readline().strip().split("-")
        fresh.append((int(line[0]), int(line[1])))
    blank = f.readline().strip()
    for _ in range(availableLines):
        available.append(int(f.readline().strip()))

# print(fresh)
# print(available)


def checkAvailable(a):
    for s,e in fresh:
        if s==a or e==a: return True
        if s<a<e: return True
    return False


ans = 0
for a in available: 
    ans += int(checkAvailable(a))
print(ans)


    
