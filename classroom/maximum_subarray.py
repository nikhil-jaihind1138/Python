class Solution(object):
    def maxSubArray(self, nums):

        # Method 1
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

        # Method 2
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = Solution()
s = obj.maxSubArray(nums)
print(s)
