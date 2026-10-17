class Solution:
    def rob(self, nums: List[int]) -> int:
        array1 = []
        array2 = []
        n = len(nums)
        if n == 1:
            return nums[0]
        if n ==2:
            return max(nums[0], nums[1])
        for i in range(0, n-1):
            array1.append(nums[i])
        for i in range(1,n):
            array2.append(nums[i])
        res = 0
        dp = [0] * (n-1)
        dp[0] = array1[0]
        dp[1] = max(dp[0], array1[1])
        for i in range(2, len(array1)):
            dp[i] = max(dp[i-1], array1[i] + dp[i-2])
        res = dp[-1]
        dp = [0] * (n-1)
        dp[0] = array2[0]
        dp[1] = max(dp[0], array2[1])
        for i in range(2, len(array2)):
            dp[i] = max(dp[i-1], array2[i] + dp[i-2])
        res = max(res, dp[-1])
        return res
