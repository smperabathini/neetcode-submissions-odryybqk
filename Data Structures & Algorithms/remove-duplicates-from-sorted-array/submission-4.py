class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        prev = nums[0]
        for r in range(1, len(nums)):
            if nums[r] != prev:
                nums[l] = nums[r]
                l += 1
                prev = nums[r]
        return l


