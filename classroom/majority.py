class Solution(object):
    def majorityElement(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums) // 2:
                return nums[i]


nums = [3, 2, 3]
obj = Solution()
s = obj.majorityElement(nums)
print(s)