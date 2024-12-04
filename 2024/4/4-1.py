numLines = 140
lines = [input() for _ in range(numLines)]
total = 0
xmas = ["XMAS", "SAMX"]
rowLen = len(lines[0])
colLen = len(lines)
#horizontal 
for row in lines:
    for i in range(rowLen-3):
        if row[i:i+4] in xmas: total += 1
#vertical (backwards and forwards)
for col in range(colLen):
    for i in range(colLen-3):
        if "".join([lines[j][col] for j in range(i, i+4)]) in xmas: total += 1
#diagonal left to right down(backwards and forwards)
for row in range(colLen-3):
    for col in range(rowLen-3):
        if "".join([lines[row+j][col+j] for j in range(4)]) in xmas: total += 1
#diagonal right to left down(backwards and forwards)
for row in range(colLen-3):
    for col in range(3,rowLen):
        if "".join([lines[row+j][col-j] for j in range(4)]) in xmas: total += 1
print(total)