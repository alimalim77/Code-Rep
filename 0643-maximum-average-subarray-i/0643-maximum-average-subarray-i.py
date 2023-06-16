class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_start,win_end,total = 0,0,0
        
        res = float("-inf")
        while win_end < len(nums):
            if win_end - win_start + 1 > k:
                total -= nums[win_start] 
                win_start += 1
            total += nums[win_end]
            
            if win_end - win_start + 1 == k:
                avg = total/k
                res = max(res,avg)
            win_end += 1
        return res
        
            