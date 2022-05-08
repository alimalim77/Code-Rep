class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final=nums1+nums2
        final.sort()
        if len(final)%2==0:
            mid=len(final)//2
            return (final[mid]+final[mid-1])/2
        mid=(len(final))//2
        return final[mid]