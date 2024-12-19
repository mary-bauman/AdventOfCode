class eleven:
    def __init__(self):
        self.memoEven = {}
        self.memoOdd = {}
        self.memoOdd[0] = 1
        self.memoEvenFive = {}
        self.memoOddFive = {}
        self.memoOddFive[0] = [4048, 1, 4048, 8096]
        self.memoOddFive[17] = [4048, 1, 4048, 8096, 28, 67, 60, 32]
        self.memoEvenFive[2024] = [4, 0, 4, 8, 20, 24, 4, 0, 4, 8, 8, 0, 9, 6]
        self.memoEvenFive[2701] = [4, 0, 4, 8, 2867, 6032, 4048, 1, 4048, 8096]
        self.memoEvenFive[781524] = [64755856, 52332544, 43447184, 58, 24]
        self.memoOddFive[9959979] = [82582, 86344, 1884344, 1829696]
        self.memo25 = {}

    def blink(self, stones):
        newStones = []
        for s in stones:
            if len(str(s))%2==1:
                if s not in self.memoOdd:
                    self.memoOdd[s] = s*2024
                newStones.append(self.memoOdd[s])
            else:
                if s in self.memoEven:
                    left, right = self.memoEven[s]
                else:
                    left = int(str(s)[:len(str(s))//2])
                    right = int(str(s)[len(str(s))//2:])
                    self.memoEven[s] = (left, right)
                newStones.append(left)
                newStones.append(right)
        return newStones
    
    def blinkFive(self, stones):
        newStones = []
        for s in stones:
            # print(f"s = {s}")
            if len(str(s))%2==1:
                if s in self.memoOddFive:
                    newStones += self.memoOddFive[s]
                else:
                    stones2 = [s]
                    for _ in range(5):
                        stones2 = self.blink(stones2)
                    self.memoOddFive[s] = stones2
                    newStones += (stones2)
            else:
                if s in self.memoEvenFive:
                    newStones += self.memoEvenFive[s]
                else:
                    stones2 = [s]
                    for _ in range(5):
                        stones2 = self.blink(stones2)
                    self.memoEvenFive[s] = stones2
                    newStones += (stones2)
            # print(f"newStones = {newStones}")
        return newStones

    
    def blink25(self, stones):
        newStones = []
        for s in stones:
            if s in self.memo25:
                newStones += self.memo25[s]
            else:
                if len(str(s))%2==1:
                    stones2 = [s]
                    for _ in range(5):
                        stones2 = self.blinkFive(stones2)
                    self.memo25[s] = stones2
                    newStones += (stones2)
                else:
                    stones2 = [s]
                    for _ in range(5):
                        stones2 = self.blinkFive(stones2)
                    self.memo25[s] = stones2
                    newStones += (stones2)
            # print(f"newStones = {newStones}")
        return newStones


from time import time
t = time()
stones = input().split()
stones = [int(s) for s in stones]
e = eleven()
# for i in range(5):
#     stones = e.blinkFive(stones)

stones25 = e.blink25(stones)
print(stones25)


# print(f"{time()-t:.5f} seconds")