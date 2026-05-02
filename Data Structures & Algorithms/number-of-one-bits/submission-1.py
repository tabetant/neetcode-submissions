class Solution:
    def hammingWeight(self, n: int) -> int:
        x = n
        coun = 0
        while x != 0:
            if x % 2 == 1:
                coun += 1
            x //= 2
        return coun