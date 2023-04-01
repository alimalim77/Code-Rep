class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        def help(i,j,nums):
            mid = (i+j)//2
            if i>j:
                return -1
            elif nums[mid] < target:
                return help(mid+1,j,nums)
            elif nums[mid] > target:
                return help(i,mid-1,nums)
            elif nums[mid] == target:
                return mid
        return help(i,j,nums)
            