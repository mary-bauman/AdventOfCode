with open("in.txt") as f:
    hands = []
    totals = {}
    for line in f:
        line = line.strip().split()
        hand = line[0]
        bid = line[1]
        #total is how much the hand is worth
        total = -1
        counted = list(hand.count(char) for char in hand)
        #print(f"counted: {counted}")
        countTwo2 = sum(1 for item in counted if item == 2)
        countTwo1 = int(countTwo2/2)
        countJ = sum(1 for item in counted if item == "J")
        c1 = max(counted)
        c = c1 + countJ
        countTwo = countTwo1 + countJ
        status = ""
        def checkFull():
            print(f"countJ: {countJ}")
            print(f"countTwo2: {countTwo2}")
            print((c1+countJ-3)+countTwo2)
            if((c1+countJ-3)+countTwo2>=2):
                return True
            return False
        if(c>=5):
            status = "five"
        elif(c==4):
            status = "four"
        elif(c>=3 and countTwo>=1 and checkFull()):
            status = "full"
        elif(c==3):
            status = "three"
        elif countTwo==2:
            status = "twoPair"
        elif(c==2):
            status = "pair"
        else:
            status = "high"
        if status in totals:
            totals[status].append((hand,bid))
        else:
            totals[status] = [(hand,bid)]
        hands.append((hand, bid))
    #print(f"hands: {hands}")
    print(f"totals: {totals}")
order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
rankedList = []
keys = ["high", "pair", "twoPair", "three", "full", "four", "five"]
for key in keys:
    if key in totals:
        if(len(totals[key])==1):
            rankedList.append(totals[key])
        else:
            # print(f"multiple {key}")
            sorted_list = sorted(list(totals[key]), key=lambda x: [order.index(c) if c in order else float('inf') for c in x[0]])
            sorted_list.reverse()
            # print(f"sorted_list: {sorted_list}")
            for s in sorted_list:
                rankedList.append(s)
# print(f"rankedListBEFORE: {rankedList}")
for r in range(len(rankedList)):
    if(len(rankedList[r])==1):
        rankedList[r] = rankedList[r][0]
#         print(f"rankedList[r] is NOW: {rankedList[r]}")
# print(f"rankedListAFTER: {rankedList}")
totalWinnings = 0
for r in range(0,len(rankedList)):
    totalWinnings += int(rankedList[r][1]) * (r+1)
    # print(f"rankedList[r][1]: {rankedList[r][1]}")
    # print(f"we added {int(rankedList[r][1]) * (r+1)}")
print(f"totalWinnings: {totalWinnings}")


#250082481 too high
#250082481