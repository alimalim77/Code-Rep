class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = nums.count(i)
        ht = sorted(ht.items(), key= lambda x: x[1])
        return ht[-1][0]