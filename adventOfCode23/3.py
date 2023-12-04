rep = [([""]*140)]*140
#print(len(rep))
rep[0] = input()
rep[1] = input()
i = 1
s = 0
symbols = ["*","#","+","$","%","=","%","/","&","-","@"]
digits = ["1","2","3","4","5","6","7","8","9","0"]
trueNums= [0]*20000
ti = 0
#lets check first line
curDigit = ""
for aa in range(0,len(rep[0])):
    a = str(rep[0][aa])
    if (a in digits):
        curDigit+=a
    else:
        part = False
        #if(curDigit != ""):
        y = len(curDigit)
        for b in range(0,y+1):
            if(rep[i][aa-b] in symbols):
                part = True
            if(aa>0):
                if(rep[i][aa-b-1] in symbols):
                    part = True
                if(rep[i-1][aa-b-1] in symbols):
                    part = True
        if(aa<(len(rep[i-1])-1)):
            if(rep[i-1][aa+1] in symbols):
                part = True
            if(rep[i][aa+1] in symbols):
                part = True
        if(curDigit!=""):
                #s+=int(curDigit)
                print(str(curDigit) + " is " + str(part))
                if(part):
                    trueNums[ti] = int(curDigit)
                    ti+=1
        curDigit = ""
        part = False

i = 2

while(i<140):
    #checking i-1
    rep[i] = input()
    r = rep[i-1]
    rr = len(r)
    curDigit = ""
    for aa in range(0,rr):
        a = str(r[aa])
        if (a in digits):
            curDigit+=a
        else:
            part = False
            if(curDigit != ""):
                y = len(curDigit)
                #start at 1 bc we're one token ahead already
                for b in range(0,y+2):
                    if(rep[i-2][aa-b] in symbols or rep[i-1][aa-b] in symbols):
                        part = True
                    if(rep[i-1][aa-b] in symbols or rep[i-1][aa-b] in symbols):
                        part = True
                    if(rep[i][aa-b] in symbols):
                        part = True
                if(rep[i-2][aa] in symbols):
                    part = True
                if(rep[i-1][aa] in symbols):
                    part = True
                if(rep[i][aa] in symbols):
                    part = True
                print(str(curDigit) + " is " + str(part))
            if(curDigit!=""):
                #s+=int(curDigit)
                if(part):
                    trueNums[ti] = int(curDigit)
                    ti+=1
                curDigit = ""
            part = False
    
    #here
    part = False
    if(curDigit != ""):
        y = len(curDigit)
        for b in range(0,y):
            if(rep[i-2][aa-b] in symbols):
                part = True
            if(rep[i][aa-b] in symbols):
                part = True
            if(aa>0):
                if(rep[i][aa-b-1] in symbols):
                    part = True
                if(rep[i-1][aa-b-1] in symbols):
                    part = True
                if(rep[i-2][aa-b-1] in symbols):
                    part = True
        if(aa<(len(rep[i-1])-1)):
            if(rep[i-2][aa+1] in symbols):
                part = True
            if(rep[i-1][aa+1] in symbols):
                part = True
            if(rep[i][aa+1] in symbols):
                part = True
        print(str(curDigit) + " is " + str(part))
    if(curDigit!=""):
        #s+=int(curDigit)
        if(part):
            trueNums[ti] = int(curDigit)
            ti+=1
        curDigit = ""
    part = False
                 


    i+=1
    

#lets check last line
#checking i-1
r = rep[i-1]
rr = len(r)
curDigit = ""
for aa in range(0,rr):
    a = str(r[aa])
    if (a in digits):
        curDigit+=a
    else:
        part = False
        if(curDigit != ""):
            y = len(curDigit)
            for b in range(0,y+1):
                if(rep[i-1][aa-b] in symbols):
                        part = True
                if(rep[i-2][aa-b] in symbols):
                    part = True
                if(aa>0):
                    if(rep[i-1][aa-y-1] in symbols):
                        part = True
                    if(rep[i-2][aa-y-1] in symbols):
                        part = True
                if(aa<(rr-1)):
                    if(rep[i-1][aa+1] in symbols):
                        part = True
                    if(rep[i-2][aa+1] in symbols):
                        part = True

            print(str(curDigit) + " is " + str(part))
        if(part and curDigit!=""):
            #s+=int(curDigit)
            trueNums[ti] = int(curDigit)
            ti+=1
        curDigit = ""
        part = False
part = False
if(curDigit != ""):
    y = len(curDigit)
    for b in range(0,y+1):
        if(rep[i-2][aa-b] in symbols):
            part = True
        if(rep[i][aa-b] in symbols):
            part = True
        if(aa>0):
            if(rep[i][aa-b] in symbols):
                part = True
            if(rep[i-1][aa-b] in symbols):
                part = True
            if(rep[i-2][aa-b] in symbols):
                part = True
        if(aa<(len(rep[i-1])-1)):
            if(rep[i-2][aa-b] in symbols):
                part = True
            if(rep[i-1][aa-b] in symbols):
                part = True
            if(rep[i][aa-b] in symbols):
                part = True
    print("digits is " + str(curDigit))
    print("part = " + str(part))
if(curDigit!=""):
    #s+=int(curDigit)
    if(part):
        trueNums[ti] = int(curDigit)
        ti+=1

    curDigit = ""
part = False

#print(trueNums)
print(sum(trueNums))
#print("s = " + str(s))

#attempt: 521740
#daniel gets 521601 and now thats what i get