class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hs = set(nums)
        for num in nums:
            if num - 1 not in hs:
                start = num
                seq = 1
                while True:
                    if start + 1 not in hs:
                        res = max(res,seq)
                        break
                    start = start + 1
                    seq += 1
        return res
