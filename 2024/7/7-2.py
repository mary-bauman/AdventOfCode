from time import time
t = time()
# numLines = 9
numLines = 850
testValues = set()
for _ in range(numLines):
    line = input().split(":")
    goal = int(line[0])
    arr = line[1].split()
    arr = [int(a) for a in arr]
    options = [[arr[0]]]
    # print(arr)
    #-1 is add, -2 is mult, -3 is combine
    for a in arr[1:]:
        newOptions = []
        for o in options:
            newOptions.append(o + [-1,a])
            newOptions.append(o + [-2,a])
            newOptions.append(o + [-3,a])
        options = newOptions
    # print(options)

    for o in options:
        cur = o[0]
        for i in range(1, len(o)-1,2):
            if o[i] == -1: cur += o[i+1]
            elif o[i] == -2: cur *= o[i+1]
            else: cur = int(str(cur) + str(o[i+1]))
        if cur == goal: testValues.add(goal)
                
# print((testValues))
print(sum(testValues))
# print((time()-t), "s")