#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        a = s.split(".")
        b = list(map(lambda x:x[::-1],a))
        c = []
        while b:
            c.append(b.pop(0))
            c.append('.')
        c.pop()
        return "".join(c)      
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends