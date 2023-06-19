class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Two For Loop - We will iterate over one then another
        result = 0 
        for i in s: # CORING the first string
            result = result ^ ord(i)
        
        for i in t: # XORING for cancellation of first string
            result = result ^ ord(i)
            
        return chr(result)