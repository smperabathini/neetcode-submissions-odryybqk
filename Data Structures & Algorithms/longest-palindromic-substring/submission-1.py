class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            if s[l] != s[r]:
                return ""
            ret_l = l
            ret_r = r
            while l != -1 and r < len(s) and s[l] == s[r]:
                ret_l = l
                ret_r = r
                l -= 1
                r += 1
                
            return s[ret_l:ret_r+1]
        res = ""
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            word1 = expand(i,i)
            if len(word1) > len(res):
                res = word1
            word2 = expand(i,i +1)
            if len(word2) > len(res):
                res = word2
        return res