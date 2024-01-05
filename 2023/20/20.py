from collections import deque
q = deque()
d = {}
broadcaster = []
with open("in-test.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        lineList = line.split(" -> ")
        one = lineList[0]
        two = lineList[1]
        prefix = one[0]
        if(prefix!="b"):
            d[one[1:]] = two.split(", ")
        else:
            broadcaster = two.split(", ")
print(f"d = {d}")
print(f"broadcaster = {broadcaster}")



def broadCast():
    for b in broadcaster:
        q.append(b)
        print(b)

    def flipFlop(s):
        print("flipFlop")

    def conjunction(s):
        print("conjunction")


    print(f"queue = {q}")
    print(q.popleft())




amountOfBroadCasts = 1
for a in range(amountOfBroadCasts):
    broadCast()

