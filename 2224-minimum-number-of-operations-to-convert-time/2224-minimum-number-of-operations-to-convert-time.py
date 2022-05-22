class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c1,c2 = current.split(":"), correct.split(":")
        
        totTime = (int(c2[0])*60+int(c2[1]))-(int(c1[0])*60+int(c1[1]))
        print(totTime)
        passes = 0
        while totTime:
            if totTime%60 == 0:
                totTime -= 60
            elif totTime%15 == 0:
                totTime -= 15
            elif totTime%5==0:
                totTime-=5
            else:
                totTime -= 1
            passes += 1
        return passes