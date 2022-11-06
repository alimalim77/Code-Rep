#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        # code here
        l,r = 0,n-1
        while l < r:
            if arr[l]:
                arr[l],arr[r] = arr[r],arr[l]
                r -= 1
            else:
                l += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends