class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        indices = []
        result = []

        def backtrack(start, current):
            if sorted(current) not in indices:
                indices.append(sorted(current[:]))
            for i in range(start, len(nums)):
                if i not in current:
                    current.append(i)
                    backtrack(i+1, current)
                    current.pop()

        backtrack(0, [])
        for i in indices:
            r = []
            for idx in i:
                r.append(nums[idx])
            if sorted(r) not in result:
                result.append(sorted(r))
            
        return result