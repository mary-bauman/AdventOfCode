with open("in-test-2.txt") as f:
    line = list(f.readline().strip('\n'))
    # print(line)
    i = 0
    while (len(set(line[i:i+14]))<14): i+=1

    print(i+14)
    
        
    
