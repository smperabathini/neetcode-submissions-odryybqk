class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n + 1):
            temp = two 
            two = one + two
            one = temp
        return two

        