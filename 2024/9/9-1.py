line = input()
files = []
space = []
for i in range(len(line)):
    if i%2==0: files.append(line[i])
    else: space.append(line[i])

s = []
for i in range(len(space)):
    for _ in range(int(files[i])): s.append(str(i))
    for _ in range(int(space[i])): s.append(".")
if len(files)>len(space):
    for _ in range(int(files[-1])): s.append(str(len(files)-1))
finalS = []
i = 0
n = len(s)
while i < n:
    if s[i] != ".":
        finalS.append(s[i])
    else:
        while s[n-1] == "." and n>0: n-=1
        finalS.append(s[n-1])
        n-=1
    i+=1
    
total = 0
for i in range(len(finalS)):
    total += int(finalS[i]) * (i)
print(total)



