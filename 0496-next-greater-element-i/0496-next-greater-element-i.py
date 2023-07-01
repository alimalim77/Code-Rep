class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        isPresent = {}
        for i in range(len(nums1)):
            isPresent[nums1[i]] = i
        isConsidered = -1
        seen = False
        
        res = []
        for i in range(len(nums1)):
            if nums1[i] not in isPresent:
                res.append(-1)
                continue
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    seen = True
                if seen and nums2[j] > nums1[i]:
                    isConsidered = nums2[j]
                    break
            res.append(isConsidered)
            isConsidered = -1
            seen = False
        return res
                
        