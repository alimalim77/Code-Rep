class UnionFind:
    # Constructor of Union-find. The size is the length of the root array.
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = []
        obj = UnionFind(len(isConnected))
        print(obj.root)
        for index in range(len(isConnected)):
            for ind2,val2 in enumerate(isConnected[index]):
                if ind2 != index and val2:
                    obj.union(index,ind2)
        count = 0
        for i,j in enumerate(obj.root):
            if i==j:
                count += 1
        return count
            
        print(obj.root)