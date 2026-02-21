with open("in.txt") as f:
  dial = 50
  numLines = 4493
  ans = 0
  for _ in range(numLines):
    line = f.readline().strip()
    if dial == 100 or dial == 0:
      ans += 1
      if line[0] == 'L': dial = 100
      if line[0] == 'R': dial = 0
    if line[0]=='L':
      dial -= int(line[1:])
      while dial < 0:
        ans += 1
        dial += 100
    elif line[0]=='R':
      dial += int(line[1:])
      while dial > 100:
        ans += 1
        dial -= 100

  print(ans)