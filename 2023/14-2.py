print(1000000000%4)

inputLen = 10
a = [""] * inputLen
available = [0] * inputLen
Ocount = 0
rowLen = 0
totals = [0] * inputLen
for i in range(0,inputLen):
    a[i] = input()
    rowLen = len(a[i])
    available[i] = sum(char != "#" for char in a[i])
    Ocount += sum(char == "O" for char in a[i])

    totals[i] = sum(char == "O" for char in a[i]) * (inputLen-i)

print(f"{sum(totals)} totals = ")
for tti in range(len(totals)):
    tt = totals[tti]
    print(f"{(inputLen-tti)} {tt}")

for aa in range(inputLen):
    print(f" {a[aa]}")

print(" ")
#count the rows
count = 0
for b in range(inputLen):
    rowCount = (inputLen-b)
    print(f"{a[b]}")
    if(Ocount>available[b]):
        count += (int(available[b]) * rowCount)
        Ocount -= available[b]
    else:
        count += (int(Ocount) * rowCount)
        Ocount = 0
    

print(f"count = {count}")
