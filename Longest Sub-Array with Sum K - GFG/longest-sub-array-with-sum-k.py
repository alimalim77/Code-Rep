#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        ht = {0:-1}
        a, st = 0,0
        for i in range(N):
            st += A[i]
            
            if st not in ht:
                ht[st] = i
            if st-K in ht:
                a = max(a,i-ht[st-K])
        return a


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends