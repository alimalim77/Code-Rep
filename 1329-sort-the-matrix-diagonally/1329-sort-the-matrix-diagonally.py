class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hm = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j not in hm:
                    hm[i-j] = []
                    hm[i-j].append(mat[i][j])
                else:
                    hm[i-j].append(mat[i][j])
        ret = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for i,j in hm.items():
            hm[i] = sorted(j)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j in hm:
                    ret[i][j] = hm[i-j].pop(0)
        return ret
                