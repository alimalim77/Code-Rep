class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        
        i = 3
        ctr = 2
        while i <= n:
            if i == n:
                return True
            else:
                i = 3**ctr
                ctr += 1
        return False