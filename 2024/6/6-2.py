# from time import time
# t = time()

class Six:
    def __init__(self):
        lines = 130
        # lines = 10
        self.arr = []
        for _ in range(lines): self.arr.append(input())
        self.rows = lines
        self.cols = len(self.arr[0])
        self.a = 0
        self.b = 0
        self.d = 0

        for a2 in range(len(self.arr)):
            if '^' in self.arr[a2]:
                self.a = a2
                self.b = self.arr[a2].index('^')
                self.d = 0
            elif '>' in self.arr[a2]:
                self.a = a2
                self.b = self.arr[a2].index('>')
                self.d = 1
            elif 'v' in self.arr[a2]:
                self.a = a2
                self.b = self.arr[a2].index('v')
                self.d = 2
            elif '<' in self.arr[a2]:
                self.a = a2
                self.b = self.arr[a2].index('<')
                self.d = 3




    def checkLoop(self, obstructionR, obstructionC):
            newArr = self.arr.copy()
            newArr[obstructionR] = newArr[obstructionR][:obstructionC] + "#" + newArr[obstructionR][obstructionC+1:]
            # for self.a in newArr: print(self.a)
            # print()
            visited = set()
            a = self.a
            b = self.b
            d = self.d
            while (a,b,d) not in visited:
                if d==0:
                    if a==0: return False
                    elif newArr[a-1][b]=='#': d = 1
                    else:
                        visited.add((a,b,d))
                        a-=1
                elif d==1:
                    if b==self.cols-1: return False
                    elif newArr[a][b+1]=='#': d = 2
                    else:
                        visited.add((a,b,d))
                        b+=1
                elif d==2:
                    if a==self.rows-1: return False
                    elif newArr[a+1][b]=='#': d = 3
                    else:
                        visited.add((a,b,d))
                        a+=1
                else:
                    if b==0: return False
                    elif newArr[a][b-1]=='#': d = 0
                    else:
                        visited.add((a,b,d))
                        b-=1
            return True


#0 = up, 1 = right, 2 = down, 3 = left

s = Six()

total = 0
for r in range(s.rows):
    for c in range(s.cols):
        if s.arr[r][c]==".":
            if s.checkLoop(r,c):
                # print("loop found at", r, c)
                total += 1
print(total)
# print("Time:", 1000*(time()-t), "s")

