class Solution:
    def longestPalindrome(self, s: str) -> int:
        # We check for the occurences of character for ex: "abccccdd" has 4' c , 2 'd and 1 a
        # Whenever there are even occurences, they can be placed well on left and right (Required for palindrome)
        # A Special case if only one character has odd occurence then it is a palindrome else not
        
        #Approach: Take an hashmap and do the counting  and then check for the length
        
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
            
        count = 0
        fl = False
        for i,j in hm.items():
            if j%2 == 0:
                count += j
            elif not fl:
                count += j
                fl = True
            else:
                count += (j-1)
    
        
        
        return count
            