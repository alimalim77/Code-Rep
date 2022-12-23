class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        
        for i in ht.items():
            if i[1] > 1:
                return True
        return False