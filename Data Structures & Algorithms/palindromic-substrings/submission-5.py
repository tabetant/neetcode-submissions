class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(s, c1, c2):
            r = c2
            l = c1
            count = 0
            while r < len(s) and l >= 0 and s[r] == s[l]:
                l -= 1
                r += 1
                count += 1
            return count
        result = 0
        for i in range(len(s)):
            result += expand(s, i, i)
            result += expand(s, i, i + 1)
        return result