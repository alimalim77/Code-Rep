class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """ 
        #6,3
        first pass: 3,0
        second pass: 
        """
        def gcd(x,y): 
            while y: #O(n)
                x,y = y,x%y
            return x 
        x,y = len(str1),len(str2) #6,4
        k = gcd(x,y) #2
        
        
        gcd1,gcd2 = str1[:k],str2[:k]  #AB #O(n)
        if gcd1 == gcd2 and str1+str2 == str2+str1:  #(ABABAB)(ABAB) #(ABAB)(ABABAB)
            return gcd1
        return ""
        #"".join(str) 
        #a = []
        #a.append(i) 
        #return "".join(n) O(n)