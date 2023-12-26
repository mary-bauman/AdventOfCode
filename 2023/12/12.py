from typing import List

def check(s, nums: List[int], memo):
    nums = tuple(nums)
    if (s, nums) in memo:
        return memo[s, nums]

    if len(nums) == 0:
        no_hashtags = all(x != '#' for x in s)
        if no_hashtags:
            memo[s, nums] = 1
            return 1
        return 0
    elif len(s) == 0 and len(nums) > 0:
        memo[s, nums] = 0
        return 0

    n = int(nums[0])
    total_sum = 0

    if s[0] == ".":
        total_sum += check(s[1:], nums, memo)
    elif s[0] == "?":
        total_sum += check("." + s[1:], nums, memo)
        total_sum += check("#" + s[1:], nums, memo)
    
    elif len(s) >= n:
        no_periods = all(s[x] != "." for x in range(n))
        if no_periods and ((n < len(s) and s[n] != "#") or n >= len(s)):
            if (n <= len(s) - 1):
                total_sum += check(s[n + 1:], nums[1:], memo)
            elif len(nums) == 1:
                total_sum += 1

    memo[s, nums] = total_sum
    return total_sum

def main():
    input_len = 1000
    lines = [""] * input_len
    total_sum = 0
    memo = {}

    for i in range(input_len):
        lines[i] = input()
        line = lines[i].split(" ")
        s = line[0]
        for _ in range(4):
            s += ("?" + line[0])
        nums = line[1].split(",") * 5
        total_sum += check(s, nums, memo)

    print(total_sum)

if __name__ == "__main__":
    main()