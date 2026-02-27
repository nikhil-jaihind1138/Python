# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ans = []
#         for i in range(nums1):
#             for j in range(nums2):
#                 if nums1[i] == nums[j]:
#                     if (nums[j+1] > nums[j]):
#                         ans.append(nums[j+1])
#                 else:
#                     ans.append(-1)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        hashmap = {}
        size = -(len(nums2))
        index = -1
        while index >= size:
            data = nums2[index]
            while stack:
                if data < stack[-1]:
                    hashmap[data] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                hashmap[data] = -1
            stack.append(data)
            index -= 1
        for value in nums1:
            ans.append(hashmap[value])
        return ans
