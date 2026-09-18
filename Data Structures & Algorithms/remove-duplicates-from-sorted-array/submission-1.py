class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        prev = -10000
        while r < len(nums):
            if nums[r] == prev:
                r += 1
            elif nums[r] != nums[l]:
                nums[l] = nums[r]
                l += 1
                prev = nums[r]
                r += 1
            else:
                prev = nums[r]
                r += 1
                l += 1
        return l

