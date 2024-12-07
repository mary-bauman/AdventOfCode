def tryAdd(first, arr, cur, goal):
    if not arr: return int(cur+first)==int(goal)
    else: 
        cur += first
        if tryAdd(arr[0], arr[1:], cur, goal): return True
        if tryMultiply(arr[0], arr[1:], cur, goal): return True
        return False

def tryMultiply(first, arr, cur, goal):
    if not arr: return cur*first==goal
    else: 
        cur *= first
        if tryAdd(arr[0], arr[1:], cur, goal): return True
        if tryMultiply(arr[0], arr[1:], cur, goal): return True
        return False
    
numLines = 850
# numLines = 9
testValues = []
for _ in range(numLines):
    line = input().split(":")
    arr = line[1].split()
    arr = [int(a) for a in arr]
    if tryAdd(arr[1], arr[2:], arr[0], int(line[0])): testValues.append(int(line[0]))
    elif tryMultiply(arr[1], arr[2:], arr[0], int(line[0])): testValues.append(int(line[0]))

print(testValues)
print(sum(testValues))