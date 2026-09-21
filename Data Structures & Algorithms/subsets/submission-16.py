class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()

        backtrack(0, [])
        return result