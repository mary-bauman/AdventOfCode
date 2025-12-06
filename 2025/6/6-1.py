# with open("in-test.txt") as f:
with open("in.txt") as f:
    for _ in range(freshLines):
        line = f.readline().strip().split("-")
        