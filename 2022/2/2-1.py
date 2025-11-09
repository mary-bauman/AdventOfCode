with open("in.txt") as f:
  points = 0
  lines = 2500
  my_shape_points = {'X':1, 'Y':2, 'Z':3}
  outcome_points = {"lose":0, "draw":3, "win":6}
  for _ in range(lines):
    op, me = f.readline().strip().split()
    print("op = ", op, "me = ", me)
    if op == 'A': # rock
      if me == 'X': # rock
        points += my_shape_points[me] + outcome_points["draw"]
      elif me == 'Y': # paper
        points += my_shape_points[me] + outcome_points["win"]
      else: # scissors
        points += my_shape_points[me] + outcome_points["lose"]
    elif op == 'B': # paper
      if me == 'X': # rock
        points += my_shape_points[me] + outcome_points["lose"]
      elif me == 'Y': # paper
        points += my_shape_points[me] + outcome_points["draw"]
      else: # scissors
        points += my_shape_points[me] + outcome_points["win"]
    else: # scissors
      if me == 'X': # rock
        points += my_shape_points[me] + outcome_points["win"]
      elif me == 'Y': # paper
        points += my_shape_points[me] + outcome_points["lose"]
      else: # scissors
        points += my_shape_points[me] + outcome_points["draw"]
  print("points = ", points)


        
    
