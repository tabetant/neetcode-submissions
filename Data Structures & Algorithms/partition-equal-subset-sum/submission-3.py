class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = {0}
        for n in nums:
            new_dp = set()
            new_dp.add(n)
            for t in dp:
                new_dp.add(t)
                new_dp.add(t+n)
            dp = new_dp
            if target in dp:
                return True
        return False