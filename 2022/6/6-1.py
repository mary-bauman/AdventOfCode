with open("in.txt") as f:
    line = list(f.readline().strip('\n'))
    # print(line)
    i = 0
    while (len(set(line[i:i+4]))<4): i+=1

    print(i+4)
    
        
    
