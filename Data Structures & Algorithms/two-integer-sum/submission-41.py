class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, n in enumerate(nums):
            if n not in m:
                m[n] = i
            elif m[n] != i and target - n == n :
                return [m[n], i]
        for i, n in enumerate(nums):
            if target - n in m and m[n] != m[target - n]:
                return [m[n], m[target - n]]
        return []
        
