class eleven:
    def __init__(self):
        self.memoEven = {}
        self.memoOdd = {}
        self.memoOdd[0] = 1

    def blink(self, stones):
        newStones = []
        for s in stones:
            if len(str(s))%2==1:
                if s in self.memoOdd:
                    newStones.append(self.memoOdd[s])
                else: 
                    newStones.append(s*2024)
            else:
                if s in self.memoEven:
                    left, right = self.memoEven[s]
                else:
                    left = int(str(s)[:len(str(s))//2])
                    right = int(str(s)[len(str(s))//2:])
                newStones.append(left)
                newStones.append(right)
        return newStones
from time import time
t = time()
stones = input().split()
stones = [int(s) for s in stones]
e = eleven()
for i in range(30):
    stones = (e.blink(stones))

print(len(stones))
print(f"{time()-t:.5f} seconds")