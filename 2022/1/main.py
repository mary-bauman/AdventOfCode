# with open("in-test.txt") as f:
with open("in.txt") as f:
    line = f.readline().strip()
    a = []
    bestCal = 0
    cur = 0
    # lines = 14
    lines = 2237
    for l in range(lines):
      line = f.readline().strip()
      if line == "":
        bestCal = max(bestCal, cur)
        cur = 0
      else:
        cur += int(line)
    print(bestCal)   
    
