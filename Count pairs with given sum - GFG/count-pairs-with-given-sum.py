#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        #[1,2,3,4]
        ctr = 0
        hm = {}
        for i in range(n):
            if k-arr[i] in hm:
                ctr += hm[k-arr[i]]
            if arr[i] not in hm:
                hm[arr[i]] = 1
            else:
                hm[arr[i]] += 1
        return ctr
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if arr[i]+arr[j]==k:
        #             ctr +=1
        # return ctr 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends