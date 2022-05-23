#User function Template for python3

def isValid(s):
    #code here
    newStr = s.split(".")
    res = []
    for i in newStr:
        if i.isdigit():
            res.append(int(i))
    if len(res) != len(newStr) or len(res) != 4:
        return 0

    for i in range(len(res)):
        if str(res[i]) != newStr[i] or not 0 <= res[i] < 256:
            return 0
    return 1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends