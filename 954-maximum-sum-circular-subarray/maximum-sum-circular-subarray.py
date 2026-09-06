class Solution(object):
    def maxSubarraySumCircular(self, nums):
        currMax, maxSum, currMin, minSum, tot = -float('inf'), -float('inf'), float('inf'), float('inf'), 0

        for n in nums:
            currMax = max(n, currMax + n)
            maxSum = max(maxSum, currMax)

            currMin = min(n, currMin + n)
            minSum = min(minSum, currMin)

            tot += n

        return max(maxSum, tot - minSum) if maxSum > 0 else maxSum