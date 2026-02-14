class Solution:
    def maxArea(self, height):

        # METHOD 1

        # start = 0
        # end = len(height) - 1
        # result = -10000
        # while start < end:
        #     w = end - start
        #     h = min(height[start], height[end])
        #     ans = w * h
        #     result = max(result, ans)
        #     if height[start] < height[end]:
        #         start += 1
        #     else:
        #         end -= 1

        # return result

        # METHOD 2
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


obj = Solution()
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
r = obj.maxArea(h)
print(r)
