with open("in-test.txt") as f:
    line = f.readline().strip()
    a = []
    while line:
      a.append([x[1:-1] for x in line.split()])
    print(a)
    
        
    
