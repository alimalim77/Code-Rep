class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        ht = sorted(ht.items(),key = lambda x: x[1],reverse = True)
        ft = list()
        for i in ht:
            if k == 0:
                return ft
            ft.append(i[0])
            k -= 1
        return ft
            
        