class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
                while stack and stack[-1][1] < temp:
                    old_i, old_temp = stack.pop()
                    res[old_i] = i - old_i
                stack.append((i,temp))
        while stack:
            res[stack.pop()[0]] = 0      
        return res          
