class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        n = len(heights)
        l = 0
        r = n - 1
        while l <r:
            area = min(heights[l],heights[r]) * (r - l)
            res = max(res,area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
            