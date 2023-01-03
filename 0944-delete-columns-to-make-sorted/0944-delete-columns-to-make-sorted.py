class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count  = 0
        mat = []
        for i in range(len(strs)):
            li = []
            for j in range(len(strs[0])):
                li.append(strs[i][j])
            mat.append(li)
            
        for i in range(len(mat[0])):
            a = ord(mat[0][i])
            for j in range(len(mat)):
                if ord(mat[j][i])<a:
                    count += 1
                    break
                else:
                    a = max(a,ord(mat[j][i]))
                
        return count