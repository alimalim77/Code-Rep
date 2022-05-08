def inc(nums):
    print(nums)
    a = nums.pop()
    while nums:
        b = nums.pop()
        if b <= a:
            print("Popped")
            a = b
            continue
        else:
            return False
    return True

def dec(nums):
    print(nums)
    a = nums.pop()
    while nums:
        b = nums.pop()
        if b >= a:
            a = b
            continue
        else:
            return False
    return True
        

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        
        if inc(list(nums)):
            return True
        if dec(list(nums)):
            return True
        return False
                
                
            