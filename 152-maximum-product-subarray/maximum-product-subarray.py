
class Solution(object):
    def maxProduct(self, nums):
        cs = nums[0]
        mn = nums[0]
        os = nums[0]

        for i in range(1, len(nums)):
            prev_cs = cs
            prev_mn = mn

            cs = max(nums[i], prev_cs * nums[i], prev_mn * nums[i])
            mn = min(nums[i], prev_cs * nums[i], prev_mn * nums[i])

            os = max(os, cs)

        return os
