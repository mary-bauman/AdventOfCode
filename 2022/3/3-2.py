# with open("in-test.txt") as f:
#   lines = 6
with open("in.txt") as f:
  lines = 300
  both = 0
  for _ in range(lines//3):
    first = f.readline().strip()
    second = f.readline().strip()
    third = f.readline().strip()
    done = []
    for c in first:
      if c in second and c in third and (c not in done):
        both += ord(c) - (96 if c.islower() else 38)
        done.append(c)
    

  print(both)
    
        