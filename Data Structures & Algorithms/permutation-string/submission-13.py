class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        lo = 0
        seen = {}
        for c in s1:
            seen[c] = seen.get(c,0) + 1
        for hi in range(len(s2)):
            window[s2[hi]] = window.get(s2[hi], 0) + 1
            if hi >= len(s1) - 1:
                if window == seen:
                    return True
                window[s2[lo]] -= 1
                if window[s2[lo]] == 0:
                    del window[s2[lo]]
                lo += 1
        return False
            
            
            