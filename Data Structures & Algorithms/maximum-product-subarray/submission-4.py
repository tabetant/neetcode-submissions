class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[0] = nums[0]
        currMax, currMin = nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = currMin
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMax = max(nums[i], nums[i] * currMax, nums[i] * temp)
            dp[i] = currMax
        return max(dp)