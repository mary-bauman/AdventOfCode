from collections import Counter

# with open("in-test.txt") as f:
  # lines = 6
with open("in.txt") as f:
  lines = 300
  both = 0
  for _ in range(lines):
    line = f.readline().strip()
    first, second = line[:len(line)//2], line[len(line)//2:]
    done = []
    for c in first:
      if c not in done and c in second:
        both += ord(c) - (96 if c.islower() else 38)
        done.append(c)
    

  print(both)
    
        
    
