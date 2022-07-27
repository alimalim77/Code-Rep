class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 1
        for i in range(2):
            ans *= max(nums)-1
            nums.remove(max(nums))
        return ans
            