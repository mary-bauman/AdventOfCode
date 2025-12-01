# with open("in-test.txt") as f:
with open("in.txt") as f:
  dial = 50
  # numLines = 10
  numLines = 4493
  ans = 0
  print(f"start: dial is at {dial}, ans = {ans}")
  for _ in range(numLines):
    line = f.readline().strip()
    if line[0] == 'L': dial -= (int(line[1:]))
    else: dial += int(line[1:])
    while dial >= 100:
      ans += 1
      dial -= 100
    while dial < 0:
      ans += 1
      dial += 100
    print(f"line: {line}, dial: {dial}, ans: {ans}")
  print(ans)  
    