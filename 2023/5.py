seeds = input().split(" ")
print(f"seeds = {seeds}")

#seed to soil
label = input()
sts = [0]*10000
for i in range(3,50):
    line = input().split(" ")

#soil to fertilizer
label = input()
stf = [0]*(83-52)
for i in range(52,84):
    line = input().split(" ")
    

#fertilizer to water
label = input()
ftw = [0]*(1000)
line = input()
while(line!="water-to-light map:"):
    line = input()

#water to light
label = input()
wtl = [0]*(1000)
line = input()
while(line!="light-to-temperature map:"):
    line = input()


#light to temp
label = input()
ltt = [{}]*(1000)
ltti = 0
line = input()
while(line!="temperature-to-humidity map:"):
    ltt[ltti] = (line).split(" ")
    ltti+=1
    line = input()
temps = [0]*len(seeds)
ltti = 0
for see in seeds:
    s = int(see)
    print(f"s = {s}")
    m = 10000000000000
    for i in range(0,ltti):
        x = ltt[i]
        one = int(x[1])
        two = int(x[0])
        three = int(x[2])-1
        if(one<=s):
            if((one+three)>=s):
                if(three>0):
                    m = min(m, (two+(s-one)))                
    if(m==10000000000000):
        m = s
    print(f"m = {m}")
    temps[ltti] = m
    ltti+=1
seeds = temps[0:ltti]
print(f"ltt seeds = {seeds}")

#temp to humid
label = input()
tth = [{}]*(1000)
tthi = 0
line = input()
while(line!="humidity-to-location map:"):
    tth[tthi] = (line).split(" ")
    tthi+=1
    line = input()
humids = [0]*len(seeds)
tthi = 0
for see in seeds:
    s = int(see)
    m = 10000000000000
    for i in range(0,tthi):
        x = tth[i]
        one = int(x[1])
        two = int(x[0])
        three = int(x[2])-1
        if(one<=s):
            if((one+three)>=s):
                if(three>0):
                    m = min(m, (two+(s-one)))                
    if(m==10000000000000):
        m = s
    humids[tthi] = m
    tthi+=1
seeds = humids[0:tthi]
print(f"tth seeds = {seeds}")

#humid to location
htl = [{}]*(1000)
htli = 0
line = input()
while(line!="end"):
    #print(f"line = {line}")
    htl[htli] = (line).split(" ")
    htli+=1
    line = input()
locations = [0]*len(seeds)
loci = 0
for see in seeds:
    s = int(see)
    print(f"s = {s}")
    m = 10000000000000
    print(f"htl = {htl}")
    for i in range(0,htli):
        x = htl[i]
        one = int(x[1])
        two = int(x[0])
        three = int(x[2])-1
        if(one<=s):
            #print(f"one = {one} and three = {three}")
            if((one+three)>=s):
                if(three>0):
                    #print("(one+three)>=s")
                    m = min(m, (two+(s-one)))
                    #print(f"m = {m}")
                
    if(m==10000000000000):
        m = s
    print(f"m = {m}")
    locations[loci] = m
    loci+=1

print(f"locations = {locations}")
print(f"min(locations) = {min(locations)}")


#part 1
#attempt 1:
    # min(locations) = 539840682
    # too high
#attempt 2:
    # min(locations) = 445858986
    #too high
#attempt 3:
    #after switch of one and two
    #265316712
    #too high
#attempt 4: 
    #my dumbass realized i gotta run things through the whole thing