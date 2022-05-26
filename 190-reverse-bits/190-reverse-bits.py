class Solution:
    def reverseBits(self, n: int) -> int:
        s = []
        print(n)
        for i in range(32,0,-1):
            a = n & 1
            n = n >> 1
            s.append(str(a))
        return int("".join(s),2)
            