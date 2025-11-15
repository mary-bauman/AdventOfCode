# with open("in-test.txt") as f:
with open("in.txt") as f:
  # linesOfBoxes = 3
  linesOfBoxes = 8
  boxes = []
  for _ in range(linesOfBoxes):
    line = list(f.readline().strip('\n'))
    row = []
    for i in range(1,len(line),4):
      c = line[i]
      if c == ' ': row.append('.')
      else: row.append(c)
    boxes.append(row)

  boxes2 = [] #flip rows and columns to make it easier 
  for c in range(len(boxes[0])):
    col = []
    for r in range(len(boxes)-1,-1,-1):
      item = boxes[r][c]
      if item != '.': col.append(item)
    boxes2.append(col)
  boxes = boxes2

  for b in boxes: print(b)
  print()

  #empty lines basically
  line = f.readline()
  line = f.readline()

  # linesOfInstructions = 4 (9-5)
  linesOfInstructions = 511-10
  instructions = []
  for _ in range(linesOfInstructions):
    line = f.readline().strip().split()
    move = int(line[1])
    fro = int(line[3])-1
    to = int(line[5])-1
    instructions.append([move, fro, to])

for totalMoving,f,t in instructions:
  while totalMoving >0 and boxes[f]:
    boxes[t].append(boxes[f].pop())
    totalMoving -= 1


ans = ""
for b in boxes:
  print(b)
  ans += b[-1]
print()
print(ans)
