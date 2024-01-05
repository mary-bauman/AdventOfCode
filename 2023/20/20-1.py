from collections import deque
from collections import defaultdict
END_MODULE = "rx"
d = {}
broadcaster = []
modType = {}
lastPulse = {}
p = defaultdict(list)
with open("in.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        lineList = line.split(" -> ")
        one = lineList[0]
        two = lineList[1]
        prefix = one[0]
        if(prefix!="b"):
            destinations = two.split(", ")
            d[one[1:]] = destinations
            for dest in destinations:
                p[dest].append(one[1:])
            modType[one[1:]] = prefix
            lastPulse[one[1:]] = "low"
        else:
            broadcaster = two.split(", ")
            modType["broadcaster"] = prefix
            lastPulse["broadcaster"] = "low"
# print(f"d = {d}")
# print(f"broadcaster = {broadcaster}")



def broadCast(onOff):
    lowPulses = 0
    highPulses = 0
    q = deque()
    q.append(("broadcaster", "low", "button"))
    lowPulses += 1
    for b in broadcaster:
        #b keyOfDest were gonna get, pulse (low = default), prev command
        q.append((b, "low", "broadcaster"))
        lowPulses += 1
        # print(b)
   

    def flipFlop(s):
        print("flipFlop")

    def conjunction(s):
        print("conjunction")


    # print(f"queue = {q}")

    while(len(q)>0):
        item = q.popleft()
        #print(f"item = {item}")
        keyOfDest = item[0]
        pulse = item[1]
        prevCommand = item[2]
        if keyOfDest == END_MODULE:
            # print(f"{prevCommand} -{pulse}-> {keyOfDest}")
            continue
        prefix = modType[keyOfDest]
        # print(f"{prevCommand} -{pulse}-> {keyOfDest}")
        # if prefix == 'b':
        #     print("why does keyOfDest equal b")
        if prefix == '%':
            if pulse == "low":
                if onOff[keyOfDest] == "off":
                    for dest in d[keyOfDest]:
                        q.append((dest, "high", keyOfDest))
                        highPulses += 1
                    onOff[keyOfDest] = "on"
                    lastPulse[keyOfDest] = "high"
                else:
                    for dest in d[keyOfDest]:
                        q.append((dest, "low", keyOfDest))
                        lowPulses += 1
                    onOff[keyOfDest] = "off"
                    lastPulse[keyOfDest] = "low"
        elif prefix == '&':
            prevList = p[keyOfDest]
            allHigh = True
            for prev in prevList:
                if lastPulse[prev] == "low":
                    allHigh = False
                    break
            if allHigh:
                for dest in d[keyOfDest]:
                    q.append((dest, "low", keyOfDest))
                    lowPulses += 1
                lastPulse[keyOfDest] = "low"
            else:
                for dest in d[keyOfDest]:
                    q.append((dest, "high", keyOfDest))
                    highPulses += 1
                lastPulse[keyOfDest] = "high"
    return (lowPulses, highPulses)

        



amountOfBroadCasts = 1000
onOffStart = defaultdict(lambda: "off")
low = 0
high = 0
for a in range(amountOfBroadCasts):
    lowP, highP = broadCast(onOffStart)
    low += lowP
    high += highP
print(low * high)