ans = 0
for _ in range(5):
    line = input()
    print(line)
    #numeric value
    numValue = 0
    for i in range(len(line)):
        if line[i].isnumeric():
            numValue = numValue * 10 + int(line[i])

    #len of shortest sequence
    prevDigit = "A"
    total = 0
    #the starting dir is always A
    for dig in line:
        match dig:
            case "A":
                match prevDigit:
                    case "0":
                        #movement pad = <A
                        #dir pad = v<<A>>^A
                        #dir pad pad = 3+2+1+4+2+1+3+2=18
                        #<vA <A A >>^A vA A <^A >A
                        total += 18
                    case "4":
                        #4 -> A
                        #movement pad = >>vvA or vv>>A
                        #dir pad = vAA<AA>^A or v<AA>AA^A or <vAA>AA^A
                        #dir pad pad =
                        #3+3+1+4+4+1+2+3+2=23
                        #3+2+4+1+4+4+1+2+2=23
                        #4+2+3+1+2+2+1+2+2=19
                        total += 19
                    case "8":
                        #8 -> A
                        #movement pad = vvv>A or >vvvA
                        #dir pad = <vAAA>A^A or v<AAA>A^A or vA<AAA>^A or vA<AAA^>A
                        #dir pad pad = 
                        # 4+2+3+1+1+2+2+2+2=19
                        # 3+2+4+1+1+2+2+2+2=19
                        total += 19
                    case "9":
                        #9 -> A
                        #movement pad = vvvA
                        # #dir pad = v<AAA^>A or v<AAA>^A or <vAAA^>A or <vAAA>^A 
                        #dir pad pad 
                        #3+2+4+1+1+2+3+2=18
                        #3+2+4+1+1+2+3+2=18
                        #4+2+3+1+1+2+3+2=18
                        total += 18
            case "0":
                match prevDigit:
                    case "A":
                        #movement pad = <A
                        #dir pad = v<<A>>^A
                        #dir pad pad = 3+2+1+4+2+1+3+2=18
                        total += 18
                    case "0":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "1":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "2":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "3":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "4":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "5":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "6":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "7":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "8":
                        #8 -> 0
                        #movement pad = vvvA
                        #dir pad = <vAAA>^A
                        #dir pad pad = 4+2+3+1+1+2+3+2=18
                        total += 18
                    case "9":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "1":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "2":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "0":
                        #0 -> 2
                        #movement pad = ^A
                        #dir pad = <A>A
                        #dir pad pad = 4+4+2+2=12
                        total += 12
            case "3":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "0":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "4":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "5":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "6":
                match prevDigit:
                    case "A":
                        #movement pad = ^^A
                        #dir pad = <^AA>A
                        #dir pad pad = 4+3+2+1+2+2=14
                        total += 14
            case "7":
                match prevDigit:
                    case "A":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
            case "8":
                match prevDigit:
                    case "A":
                        #A -> 8
                        #movement pad ^^^<A or <^^^A
                        #dir pad = <AAAv<A>^>A or <AAAv<A>>^A
                        #dir pad pad = 
                        # 4+4+1+1+3+2+4+2+3+3+2=26
                        # 4+4+1+1+3+2+4+2+1+3+2=27
                        total += 26
                    case "0":
                        #0 -> 8
                        #movement pad = ^^^A
                        #dir pad = <AAA>A
                        #dir pad pad = 4+4+1+1+2+2=14
                        total += 14
                    case "1":
                        #0 -> 1
                        #movement pad = ^<A
                        #dir pad <Av<A>>^A
                        #dir pad pad = 4+4+3+2+4+2+1+3+2=25
                        total += 25
                    case "2":
                        #2 -> 8
                        #movement pad = 
                        #dir pad 
                        #dir pad pad
                        total += 0
                    case "3":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "4":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "5":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "6":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "7":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "8":
                        #movement pad
                        total += 0
                        #dir pad 
                        total += 0
                        #dir pad pad
                        total += 0
                    case "9":
                        #9 -> 8
                        #movement pad = <A
                        #dir pad = v<<A>>^A
                        #dir pad pad = 3+2+1+4+2+1+3+2=18
                        total += 18
            case "9":
                match prevDigit:
                    case "A":
                        #A -> 9
                        #movement pad = ^^^A
                        #dir pad = <AAA>A
                        #dir pad pad = 4+4+1+1+2+2=14
                        total += 14
                    case "0":
                        #0 -> 9
                        #movement pad = >^^^A
                        #dir pad = vA<^AAA>A or vA^<AAA>A
                        #dir pad pad
                        #3+3+4+3+2+1+1+2+2=21
                        #3+3+2+3+4+1+1+2+2=21
                        total += 21
                    case "1":
                        #movement pad
                        #dir pad 
                        #dir pad pad
                        total += 0
                    case "2":
                        #2 -> 9
                        #movement pad = >^^A
                        #dir pad = vA<^AA>A
                        total += 20


        #once there are no unchanging nums we have ans
        print(total)
        prevDigit = dig

    # total += 4
    print(f"total for {line} = {total}*{numValue} = {total*numValue}")    
    ans += total * numValue

print("ans = ", ans)

