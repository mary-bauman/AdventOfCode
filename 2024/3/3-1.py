
mults = []
total = 0
lines = 6
for _ in range(lines):
    s = input()
    i = 0
    n = len(s)
    while i < n-8:
        if s[i:i+4]=='mul(':
            i+=4
            between = ""
            j = i
            while s[j]!=')' and j<n: between += s[j]; j+=1
            if ',' in between:
                between = between.split(',')
                a = between[0]
                b = between[1]
                if a.isdigit() and b.isdigit():
                    a = int(a)
                    b = int(b)
                    mults.append([a,b])
                    total += a*b
        i+=1


# print(mults)
print(total)