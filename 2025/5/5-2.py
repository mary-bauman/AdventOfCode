freshLines = 4
# freshLines = 169
fresh = []
# with open("in-test.txt") as f:
with open("in.txt") as f:
    for _ in range(freshLines):
        line = f.readline().strip().split("-")
        fresh.append((int(line[0]), int(line[1])))


    
