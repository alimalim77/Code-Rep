class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        visited = set()
        maxVal = float("-inf")
        for i in nums:
            count = 1
            if i-1 not in s:
                while i + 1 in s:
                    #visited.add(i+1) #201
                    count += 1 
                    i += 1
                    
            maxVal = max(maxVal,count)
        if maxVal == float("-inf"):
            return 1
        else:
            return maxVal
                
                
                