with open("in.txt") as f:
    time = f.readline().strip().split(":")[1].strip().split()
    distance = f.readline().strip().split(":")[1].strip().split()
    print(f"time = {time}")
    time = [int(x) for x in time]
    print(f"distance = {distance}")
    distance = [int(x) for x in distance]
    waysToWinMultipliedTogether = 1
    for i in range(len(time)):
        t = time[i]
        d = distance[i]
        #print(f"t = {t} d = {d}")
        #lets calculate all values 1 to (time-1) 
        #(0 = 0 and time = 0 so they don't matter)
        times = [x for x in range(t)]
        for speed in range(1,t):
            times[speed] = (speed * (t-speed))
        #print(f"times = {times}")
        wins = sum(1 for x in times if x > d)
        #print(f"wins = {wins}")
        waysToWinMultipliedTogether *= wins

print(f"waysToWinMultipliedTogether = {waysToWinMultipliedTogether}")