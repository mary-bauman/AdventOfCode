numLines = 2
with open("in-test.txt") as f:
    for _ in range (numLines) :
        line = f.readline().strip()