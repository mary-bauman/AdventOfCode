# freshLines = 4
freshLines = 169
fresh = []
# with open("in-test.txt") as f:
with open("in.txt") as f:
    for _ in range(freshLines):
        line = f.readline().strip().split("-")
        fresh.append((int(line[0]), int(line[1])))
    fresh.sort()

    done = [fresh[0]]
    for s,e in fresh:
        prevS,prevE = done[-1]
        if s <= prevE: #overlap
            done.pop()
            done.append((min(s,prevS), max(e,prevE)))
        else: done.append((s,e))

ans = sum((e - s + 1) for s, e in done)
print(ans)