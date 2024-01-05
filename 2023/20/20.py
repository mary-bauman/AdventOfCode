from collections import deque
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



def broadCast(onOff):
    q = deque()
    q.append(("broadcaster", "low", "button"))
    for b in broadcaster:
        #b key were gonna get, pulse (low = default), prev command
        q.append((b, "low", "broadcaster"))
        print(b)
   

    def flipFlop(s):
        print("flipFlop")

    def conjunction(s):
        print("conjunction")


    print(f"queue = {q}")

    while(len(q)>0):
        item = q.popleft()
        #print(f"item = {item}")
        key = item[0]
        pulse = item[1]
        prevCommand = item[2]
        print(f"{prevCommand}  -{pulse}-> {key}")


        



amountOfBroadCasts = 1
onOffStart = {}
for b in broadcaster:
    onOffStart[b] = "off"
for a in range(amountOfBroadCasts):
    broadCast(onOffStart)

