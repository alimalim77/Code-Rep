class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row Check
        s1 = set()
        r = len(board)
        c = len(board[0])
        for i in range(len(board)):
            a = []
            for i in board[i]:
                if i.isdigit():
                    a.append(i)
            if len(set(a)) != len(a):
                return False
        
        tpboard = list(zip(*board))
        for i in range(r):
            a = []
            for i in tpboard[i]:
                if i.isdigit():
                    a.append(i)
            if len(set(a)) != len(a):
                return False
            
        ht = {}
        for i in range(r):
            for j in range(c):
                if (r//3,c//3) not in ht:
                    ht[(i//3,j//3)] = set()
        
        
        for i in range(0,r):
            for j in range(0,c):
                if board[i][j] == '.':
                    continue
                if board[i][j] in ht[(i//3,j//3)]:
                    return False
                ht[(i//3,j//3)].add(board[i][j])
                #print(ht)
                #print("\n")
        #print(ht)
        return True