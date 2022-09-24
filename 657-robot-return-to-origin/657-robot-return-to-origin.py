# [Longtitude, Latitude]
# [0,0]

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        curPos = [0,0]
        
        for i in moves:
            if i == "U":
                curPos[0] += 1
            elif i == "D":
                curPos[0] -= 1
            elif i == "R":
                curPos[1] += 1
            elif i == "L":
                curPos[1] -= 1
        
        if curPos == [0,0]:
            return True
        else: return False
                
                
        
        
        