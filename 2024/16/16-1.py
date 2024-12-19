class Sixteen:
    def __init__(self):
        self.e = (0,0)
        self.numCols = 0
        self.numLines = 0
        self.maze = []


    def findScore(self, row, col, facing, done):
        if (row,col,facing) in done: return -1
        done.add((row,col,facing))
        if row<0 or row>=self.numLines or col<0 or col>=self.numCols: return -1
        if maze[row][col] == '#': return -1
        if (row,col) == self.e:
            print()
            print("just this one")
            print()
            for d in done: print(d)
            return 0
        match facing:
            case "right":
                down = 1000 + self.findScore(row+1, col, "down",done)
                up = 1000 + self.findScore(row-1, col, "up",done)
                forward = self.findScore(row, col+1, "right",done)
                twoTurnsLeft = 2000 + self.findScore(row, col-1, "left",done)
                ans = -1
                if twoTurnsLeft != 1999: ans = twoTurnsLeft
                if down != 999:
                    if ans == -1: ans = down
                    else: ans = min(ans, down)
                if up != 999:
                    if ans == -1: ans = up
                    else: ans = min(ans, up)
                if forward != -1:
                    if ans == -1: ans = forward
                    else: ans = min(ans, forward)
                return ans
            case "left":
                down = 1000 + self.findScore(row+1, col, "down",done)
                up = 1000 + self.findScore(row-1, col, "up",done)
                forward = self.findScore(row, col-1, "left",done)
                twoTurnsRight = 2000 + self.findScore(row, col+1, "right",done)
                ans = -1
                if twoTurnsRight != 1999: ans = twoTurnsRight
                if down != 999:
                    if ans == -1: ans = down
                    else: ans = min(ans, down)
                if up != 999:
                    if ans == -1: ans = up
                    else: ans = min(ans, up)
                if forward != -1:
                    if ans == -1: ans = forward
                    else: ans = min(ans, forward)
                return ans
            case "down":
                right = 1000 + self.findScore(row, col+1, "right",done)
                left = 1000 + self.findScore(row, col-1, "left",done)
                forward = self.findScore(row+1, col, "down",done)
                twoTurnsUp = 2000 + self.findScore(row-1, col, "up",done)
                ans = -1
                if twoTurnsUp != 1999: ans = twoTurnsUp
                if right != 999:
                    if ans == -1: ans = right
                    else: ans = min(ans, right)
                if left != 999:
                    if ans == -1: ans = left
                    else: ans = min(ans, left)
                if forward != -1:
                    if ans == -1: ans = forward
                    else: ans = min(ans, forward)
                return ans
            case "up":
                right = 1000 + self.findScore(row, col+1, "right",done)
                left = 1000 + self.findScore(row, col-1, "left",done)
                forward = self.findScore(row-1, col, "up",done)
                twoTurnsDown = 2000 + self.findScore(row+1, col, "down",done)
                ans = -1
                if twoTurnsDown != 1999: ans = twoTurnsDown
                if right != 999:
                    if ans == -1: ans = right
                    else: ans = min(ans, right)
                if left != 999:
                    if ans == -1: ans = left
                    else: ans = min(ans, left)
                if forward != -1:
                    if ans == -1: ans = forward
                    else: ans = min(ans, forward)
                return ans
            case _:
                return -1

            

st = Sixteen() 
st.numLines = 15
maze = [input() for _ in range(st.numLines)]
st.maze = maze
st.numCols = len(maze[0])
s = (0,0)
for row in range(st.numLines):
    for col in range(st.numCols):
        if maze[row][col] == 'S':
            s = (row, col)
        if maze[row][col] == 'E':
            st.e = (row, col)
print(s)
print(st.findScore(s[0], s[1], "right",set()))