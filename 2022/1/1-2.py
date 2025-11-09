# with open("in-test.txt") as f:
with open("in.txt") as f:
    line = f.readline().strip()
    cals = []
    cur = 0
    # lines = 14
    lines = 2237
    for l in range(lines):
      line = f.readline().strip()
      if line == "":
        cals.append(cur)
        cur = 0
      else:
        cur += int(line)
    cals.sort(reverse=True)
    for c in cals[:3]:
      print(c)
    print(sum(cals[:3]))
    
