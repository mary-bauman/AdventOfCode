#https://adventofcode.com/2023/day/2
sum = 0
for a in range(1,101):
    game = input().split(":")
    rounds = game[1].split(";")
    #print(rounds)
    red = 0
    green = 0
    blue = 0
    for round in rounds:
        #print(round)
        digit = ""
        c = 0
        while(c < len(round)):
            #print("digit = " + str(digit))
            char = str(round[c])
            if(char=="r"):
                #print("digit2 = " + str(digit))
                #print(red)
                if(int(digit)>int(red)):
                    red = int(digit)
                digit = ""
                c+=3
            elif(char=="g"):
                if(int(digit)>int(green)):
                    green = int(digit)
                digit = ""
                c+=5
            elif(char=="b"):
                if(int(digit)>int(blue)):
                    blue = int(digit)
                digit = ""
                c+=4
            elif(char==","):
                digit = ""
                c+=1
            elif(char==" "):
                c+=1
            elif(char.isdigit):
                #print(char + " is digit")
                digit+=char
                c+=1
            else:
                c+=1



    power = red * green * blue
    print("red = " + str(red))
    print("power = " + str(power))
    sum+=power   
print("sum = " + str(sum))


    
