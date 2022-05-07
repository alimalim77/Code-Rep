class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        
        def sortednum(num):
            s = sorted(num)
            return "".join(s)
        
        for i in strs:
            a = sortednum(i)
            if a not in ht:
                ht[a] = []
        
        for i in strs:
            b = sortednum(i)
            if b in ht:
                ht[b].append(i)
        final = []
        for i,j in ht.items():
            final.append(j)
        return final
            