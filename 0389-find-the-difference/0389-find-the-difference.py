# t o d a y - S
# d a s t o y - T
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set1 = Counter(s)
        set2 = Counter(t)
        
        for i in set2:
            if set1[i] != set2[i] or i not in set1:
                return i
        
        
        