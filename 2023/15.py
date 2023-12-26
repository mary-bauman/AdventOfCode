a = input().split(",")
totals = [0] * len(a)
for b in range(len(a)):
    val = 0
    for letter in a[b]:
        ascii = ord(letter)
        val+= ascii
        val*=17
        val = val % 256
    totals[b] = val

print(f"{sum(totals)} totals = {totals}")