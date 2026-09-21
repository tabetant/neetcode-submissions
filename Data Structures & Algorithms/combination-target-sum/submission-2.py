class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, current):
            if sum(current) == target and sorted(current) not in result:
                result.append(sorted(current))
            elif sum(current) > target:
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current)
                current.pop()
        backtrack(0, [])
        return result