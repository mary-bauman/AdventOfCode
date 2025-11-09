with open("in.txt") as f:
  points = 0
  lines = 2500
  outcome_points = {'X':0, 'Y':3, 'Z':6}
  shape_points = {'A':1, 'B':2, 'C':3}

  for _ in range(lines):
    op, outcome = f.readline().strip().split()
    if outcome == 'X': #lose
      if op == 'A': #op chose rock
        points += outcome_points[outcome] + shape_points['C']
      elif op == 'B': #op chose paper
        points += outcome_points[outcome] + shape_points['A']
      else: #op chose scissors
        points += outcome_points[outcome] + shape_points['B']
    elif outcome == 'Y': #draw
      points += outcome_points[outcome] + shape_points[op]
    else: #win
      if op == 'A': #op chose rock
        points += outcome_points[outcome] + shape_points['B']
      elif op == 'B': #op chose paper
        points += outcome_points[outcome] + shape_points['C']
      else: #op chose scissors
        points += outcome_points[outcome] + shape_points['A']
      
      

    
  print(points)