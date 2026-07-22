class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=[]
        for i in sorted(set(nums1)):
            for j in sorted(set(nums2)):
                if i==j:
                    num.append(i)
        return num