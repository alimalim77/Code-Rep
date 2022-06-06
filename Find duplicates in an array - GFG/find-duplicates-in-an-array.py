class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	hm = {} #map
    	for i in arr:
    	    if i not in hm:
    	        hm[i] = 1
    	    else:
    	        hm[i] += 1
        li = list()
        for i,j in hm.items():
            if j > 1:
                li.append(i)
        li.sort()
        return li if len(li) > 0 else [-1]
    	
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends