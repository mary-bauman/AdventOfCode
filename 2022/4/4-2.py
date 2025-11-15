# with open("in-test.txt") as f:
#   lines = 6
with open("in.txt") as f:
  lines = 1000
  ans = 0
  for _ in range(lines):
    one, two = f.readline().strip().split(",")
    s1, b1 = map(int, one.split("-"))
    s2, b2 = map(int, two.split("-"))
    if s1 <= s2 and b1 >= b2: ans +=1
    elif s2 <= s1 and b2 >= b1: ans +=1
    elif s1<=s2 and b1>=s2: ans +=1
    elif s2<=s1 and b2>=s1: ans +=1

  print(ans)
        
    
