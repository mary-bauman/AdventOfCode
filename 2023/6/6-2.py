with open("in.txt") as f:
    time = f.readline().strip().split(":")[1].strip().split()
    time = int(''.join(time))
    d = f.readline().strip().split(":")[1].strip().split()
    d = int(''.join(d))
    print(f"time = {time}")
    print(f"distance = {d}")
    total = 0
    for speed in range(time):
        if(speed*(time-speed) > d):
            total += 1
    print(f"total = {total}")
    
        
    
