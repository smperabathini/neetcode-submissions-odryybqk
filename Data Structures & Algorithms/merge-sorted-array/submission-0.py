class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m - 1
        r = n - 1
        pos = len(nums1) - 1
        while l > -1 and r > -1:
            if nums2[r] >= nums1[l]:
                nums1[pos] = nums2[r]
                r -= 1
                pos -= 1
            else:
                nums1[pos] = nums1[l]
                l -= 1
                pos -= 1
        while r > -1:
            nums1[pos] = nums2[r]
            r -= 1
            pos -= 1            


        