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


def broadCast(onOff):
    q = deque()
    q.append(("broadcaster", "low", "button"))
    for b in broadcaster:
        q.append((b, "low", "broadcaster"))

    while(len(q)>0):
        endFound = False
        item = q.popleft()
        keyOfDest = item[0]
        pulse = item[1]
        if keyOfDest == END_MODULE:
            #print(f"{item[2]} -{pulse}-> {keyOfDest}")
            if(pulse=="low"):
                endFound = True
            continue
        prefix = modType[keyOfDest]
        if prefix == '%':
            if pulse == "low":
                if onOff[keyOfDest] == "off":
                    for dest in d[keyOfDest]:
                        q.append((dest, "high", keyOfDest))
                    onOff[keyOfDest] = "on"
                    lastPulse[keyOfDest] = "high"
                else:
                    for dest in d[keyOfDest]:
                        q.append((dest, "low", keyOfDest))
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
                lastPulse[keyOfDest] = "low"
            else:
                for dest in d[keyOfDest]:
                    q.append((dest, "high", keyOfDest))
                lastPulse[keyOfDest] = "high"
    return (endFound)

onOffStart = defaultdict(lambda: "off")
count = 0
endFound = False
while not endFound:
    endFound = broadCast(onOffStart)
    count+=1
print(f"count = {count}")