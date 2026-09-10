class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, n in enumerate(nums):
            comp = target - n
            if comp in m:
                return [m[comp], i]
            m[n] = i
        return []
