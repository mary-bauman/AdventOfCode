from math import ceil
import re
total = 0
tolerance = 1/(100*100)
numLines = 1281
inp = [input()+input()+input()+input() for _ in range(ceil(numLines//4))]
for line in inp:
    #\d means a digit 0-9 and + means at least one digit
    #there is a fixed 6 digits in each set of buttons
    ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', line))
    #I got this math from https://github.com/mgtezak/Advent_of_Code/blob/master/2024/13/p1.py
    # if max(ax,bx)*100>=x and max(ay,by)*100>=y:
    a = (bx*y - by*x) / (bx*ay - by*ax)
    b = (x-ax*a) / bx
    if abs(a-round(a)) < tolerance and abs(b-round(b)) < tolerance:
        total+= 3*a + b
print(int(total))