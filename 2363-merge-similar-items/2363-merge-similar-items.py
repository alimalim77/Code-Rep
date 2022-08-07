class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = [] # to return
        hm = {}
        for i in items1:
            a,b = i
            hm[a] = b
        #print(hm)
        for i in items2:
            c,d = i
            if c in hm:
                #print(hm[c])
                hm[c] += d
            else:
                hm[c] = d
                #print(hm[c])
        ret = sorted(hm.items(),key = lambda x: x[0])
        return list(map(list,ret))