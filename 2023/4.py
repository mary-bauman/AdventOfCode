total = 219
cards = [0] * (total+1)
for cardNum in range(1,(total+1)):
    cardInfo = input().split("|")
    cardSum = 0
    front = cardInfo[0].split(":")
    winningNums = front[1].split(" ")
    nums = cardInfo[1].split(" ")
    for n in nums:
        if(n!="" and n in winningNums):
            cards[cardNum] += 1

#dp is amount you get by calling each card once
dp = [1] * (total+1)
dp[0] = 0
i = total - 1

while(i>0):
    top = min((i + cards[i]),(total))
    for y in range(i+1,(top+1)):
        dp[i] += (dp[y])
    i-=1


print("sum = " + str(sum(dp)))
print(dp)
for f in range(0,total+1):
    print("dp " + str(f) + " = " + str(dp[f]))
    print("cards " + str(f) + " = " + str(cards[f]))
    print("    ")









#attempt 4: 956787
#attempt 5: 6227972 (didnt submit bc i dont think its right)
#attempt 6: 6225785 probably too high but it worked on the og test case
#attempt 7: 6227972