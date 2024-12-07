lines=130
arr = []
for _ in range(lines): arr.append(input())
visited = []
rows = lines
cols = len(arr[0])
a = 0
b = 0
#up is 0
#right is 1
#down is 2
#left is 3
d = 0

for a2 in range(len(arr)):
    if '^' in arr[a2]:
        a = a2
        b = arr[a2].index('^')
        d = 0
    elif '>' in arr[a2]:
        a = a2
        b = arr[a2].index('>')
        d = 1
    elif 'v' in arr[a2]:
        a = a2
        b = arr[a2].index('v')
        d = 2
    elif '<' in arr[a2]:
        a = a2
        b = arr[a2].index('<')
        d = 3


while [a,b,d] not in visited:
    if d==0:
        if a==0: 
            visited.append([a,b,d])
            break
        elif arr[a-1][b]=='#':
            d = 1
        else:
            visited.append([a,b,d])
            a-=1
    elif d==1:
        if b==cols-1: 
            visited.append([a,b,d])
            break
        elif arr[a][b+1]=='#':
            d = 2
        else:
            visited.append([a,b,d])
            b+=1
    elif d==2:
        if a==rows-1: 
            visited.append([a,b,d])
            break
        elif arr[a+1][b]=='#':
            d = 3
        else:
            visited.append([a,b,d])
            a+=1
    else:
        if b==0: 
            visited.append([a,b,d])
            break
        elif arr[a][b-1]=='#':
            d = 0
        else:
            visited.append([a,b,d])
            b-=1
# print(visited)
# for a,b,d in visited:
#     arr[a] = arr[a][:b] + 'X' + arr[a][b+1:]
# for a in arr: print(a)
unique = []
for a,b,c in visited:
    if [a,b] not in unique:
        unique.append([a,b])

print(len((unique)))
    