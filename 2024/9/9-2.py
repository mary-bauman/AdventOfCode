line = input()
files = dict()
spaces = dict()
for i in range(len(line)):
    if i%2==0: files[i] = int(line[i])
    else: spaces[i] = int(line[i])

#just for debugging
arr = []
fileLen = 0
spaceLen = 0
for i in range(0,len(line)-1,2):
    # print(files[i])
    # print(spaces[i+1])
    if i in files:
        for _ in range(int(files[i])): arr.append(str(i))
        fileLen+=1
    if i+1 in spaces:
        for _ in range(int(spaces[i+1])): arr.append(".")
        spaceLen+=1

if len(line)%2==1:
    sn = len(line)//2 - 1
    for _ in range(int(files[sn])): arr.append(str(sn+1))
    fileLen+=1

for a in range(len(arr)):
    if arr[a]!='.': arr[a] = str(int(arr[a])//2)
print(''.join(arr))


print(line)

for i in range((fileLen*2)-2,-1,-2):
    for j in range(spaceLen*2-1,0,-2):
        if spaces[j]>=files[i]:
            spaces[j] -= files[i]
            if j in files: files[j] += files[i]
            else: files[j] = files[i]
            del files[i]
            break
print("files: ", files)
print("spaces: ", spaces)


#change around files and spaces



arr = []
for i in range(0,len(line)-1):
    if i in files:
        for _ in range(int(files[i])): arr.append(str(i))
    if i in spaces:
        for _ in range(int(spaces[i])): arr.append(".")
# if len(line)%2==1:
#     sn = len(line)//2 - 1
#     for _ in range(int(files[sn])): arr.append(str(sn+1))
for a in arr:
    if a!=".": a = int(a)//2
print(''.join(arr))

#checksum
total = 0
for i in range(len(arr)):
    if arr[i] != ".": total += int(arr[i]) * i//2
print(total)



