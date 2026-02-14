def maxProduct(nums):
    min_val = max_val = ans = nums[0]


# method 1
    # for i in range(1, len(nums)):
    #     d = nums[i]

        # prev_max = max_val
        # prev_min = min_val

        # max_val = max(d, prev_max * d, prev_min * d)
        # min_val = min(d, prev_max * d, prev_min * d)

        # ans = max(ans, max_val)

    # return ans

# method 2
    pmax = pmin = answer = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        if current<0:
            pmax, pmin = pmin, pmax
        pmax = max(current, pmax*current)
        pmin = min(current, pmin*current)
        answer = max(answer, pmax)
    return answer


nums = [2, 3, -2, 4]
r = maxProduct(nums)
print(r)
