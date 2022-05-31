#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        finList = [0]*n
        zero,one,two = 0,0,0
        for i in arr:
            if i == 0: zero += 1
            elif i == 1: one += 1
            else: two += 1
        i = 0
        while zero:
            arr[i] = 0
            i += 1
            zero -= 1
        while one:
            arr[i] = 1
            i += 1
            one -= 1
        while two:
            arr[i] = 2
            i += 1
            two -= 1
        return finList
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends