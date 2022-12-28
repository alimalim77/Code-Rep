import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums: # O(n)
            if i not in hm:
                hm[i] = 0
            hm[i] += 1
        
        return heapq.nlargest(k, hm.keys(), key=hm.get) #O(nlogk) 