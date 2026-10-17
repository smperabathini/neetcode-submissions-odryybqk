class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        C = [0] * (len(cost) + 1)
        C[0] = 0
        C[1] = 0
        for i in range(2, len(cost) + 1):
            C[i] = min(C[i-1] + cost[i-1], C[i-2] + cost[i-2])
        return C[len(cost)]