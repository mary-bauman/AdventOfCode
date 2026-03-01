line = "" #put input here
a = line.split(",")
for item in a:
    start, end = map(int, item.split("-"))
    for i in range(start,end+1):
        s = str(i)
        mid = len (s) // 2
        if s[mid:] == s[:mid]: 
            ans += i
print (ans)