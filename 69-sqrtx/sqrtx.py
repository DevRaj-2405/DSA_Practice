class Solution(object):
    def mySqrt(self, x):
        if x < 2:   # sqrt(0) = 0, sqrt(1) = 1
            return x

        left, right = 2, x // 2  # sqrt(x) must be in [2, x//2]
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:        # perfect square
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1

        return right   # when loop ends, right < left, so right is the floor(sqrt(x))





