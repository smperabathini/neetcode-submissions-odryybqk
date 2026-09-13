class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")": "(", "]": "[", "}": "{"}
        stack = []
        if len(s) % 2 ==1 : return False
        for char in s:
            if char not in hm.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                if hm[char] != stack.pop():
                    return False
        return True if not stack else False