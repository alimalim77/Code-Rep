class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        frst = list(map(lambda x: int(str(x)[0]), nums))
        last = list(map(lambda x: x % 10, nums))

        for i, n1 in enumerate(frst):
            for n2 in last[i + 1:]:
                if self.are_coprime(n1, n2):
                    ans += 1

        return ans

    def are_coprime(self, a, b):
        for i in range(2, max(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return False
        return True