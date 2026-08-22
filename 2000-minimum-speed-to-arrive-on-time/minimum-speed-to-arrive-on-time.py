# class Solution(object):
#     def minSpeedOnTime(self, dist, hour):
#         if len(dist) >= hour+1:
#             return -1
            
#         left=1
#         right=10**7
#         while left<right:

#             mid=(left+right)//2

#             if sum([ceil(i/mid) for i in dist[:-1]])+ dist([-1]/mid)<=hour:

#                 right=mid
#             else:

#                 left-mid+1
#         return left


class Solution(object):
    def minSpeedOnTime(self, dist, hour):

        # If there are n trains, the first n-1 trains
        # each require at least 1 full hour.
        if len(dist) - 1 >= hour:
            return -1

        left = 1
        right = 10**7

        while left < right:

            mid = (left + right) // 2

            # For the first n-1 trains, we must wait
            # until the next integer hour.
            #
            # (i + mid - 1) // mid is equivalent to ceil(i / mid)
            # without using floating-point division.
            time = sum((i + mid - 1) // mid for i in dist[:-1])

            # The LAST train does not need to be rounded up.
            # float() is important if the environment uses
            # integer division for /.
            time += float(dist[-1]) / mid

            if time <= hour:
                right = mid
            else:
                left = mid + 1

        return left
