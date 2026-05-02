class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            x = i
            coun = 0
            while x != 0:
                if x % 2 == 1:
                    coun += 1
                x //= 2
            result.append(coun)
        return result