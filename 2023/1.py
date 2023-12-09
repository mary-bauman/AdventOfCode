sum = 0
for a in range(0,1000):
    #hardcoded input length
    s = input()
    first = 0
    second = 0
    looking = True
    i = 0
    cur = "justadding"
    digit = False
    while((not digit) and i<len(s)):
        cur+=s[i]
        curi = len(cur)-1
        if(cur[(curi-3):curi] == "one"):
            digit = True
            first = 1
        elif (cur[(curi-3):curi] == "two"):
            digit = True
            first = 2
        elif (cur[(curi-5):curi] == "three"):
            digit = True
            first = 3
        elif (cur[(curi-4):curi] == "four"):
            digit = True
            first = 4
        elif (cur[(curi-4):curi] == "five"):
            digit = True
            first = 5
        elif (cur[(curi-3):curi] == "six"):
            digit = True
            first = 6
        elif (cur[(curi-5):curi] == "seven"):
            digit = True
            first = 7
        elif (cur[(curi-5):curi] == "eight"):
            digit = True
            first = 8
        elif (cur[(curi-4):curi] == "nine"):
            digit = True
            first = 9
        elif (str(s[i])=="1"):
            digit = True
            first = 1
        elif (str(s[i])=="2"):
            digit = True
            first = 2
        elif (str(s[i])=="3"):
            digit = True
            first = 3
        elif (str(s[i])=="4"):
            digit = True
            first = 4
        elif (str(s[i])=="5"):
            digit = True
            first = 5
        elif (str(s[i])=="6"):
            digit = True
            first = 6
        elif (str(s[i])=="7"):
            digit = True
            first = 7
        elif (str(s[i])=="8"):
            digit = True
            first = 8
        elif (str(s[i])=="9"):
            digit = True
            first = 9
        else:
            i += 1
        
        
    i = len(s)-1
    looking = True
    cur = "justadding"
    digit = False
    while((not digit) and i>=0):
        cur+=s[i]
        curi = len(cur)-1
        if(cur[(curi-3):curi] == "eno"):
            digit = True
            second = 1
        elif (cur[(curi-3):curi] == "owt"):
            digit = True
            second = 2
        elif (cur[(curi-5):curi] == "eerht"):
            digit = True
            second = 3
        elif (cur[(curi-4):curi] == "ruof"):
            digit = True
            second = 4
        elif (cur[(curi-4):curi] == "evif"):
            digit = True
            second = 5
        elif (cur[(curi-3):curi] == "xis"):
            digit = True
            second = 6
        elif (cur[(curi-5):curi] == "neves"):
            digit = True
            second = 7
        elif (cur[(curi-5):curi] == "thgie"):
            digit = True
            second = 8
        elif (cur[(curi-4):curi] == "enin"):
            digit = True
            second = 9
        elif (str(s[i])=="1"):
            digit = True
            second = 1
        elif (str(s[i])=="2"):
            digit = True
            second = 2
        elif (str(s[i])=="3"):
            digit = True
            second = 3
        elif (str(s[i])=="4"):
            digit = True
            second = 4
        elif (str(s[i])=="5"):
            digit = True
            second = 5
        elif (str(s[i])=="6"):
            digit = True
            second = 6
        elif (str(s[i])=="7"):
            digit = True
            second = 7
        elif (str(s[i])=="8"):
            digit = True
            second = 8
        elif (str(s[i])=="9"):
            digit = True
            second = 9
        else:
            i -= 1
    #print(first)
    #print(second)
    num = (first * 10) + second
    print("num = " + str(num))
    sum += num
print("sum = " + str(sum))
#too low rn