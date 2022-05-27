class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a  = int(str(num)[::-1])
        b = str(a)[::-1]
        return int(b) == num