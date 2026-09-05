class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        ml=float('inf')
        cnt=0

        for r in range(len(nums)):
            cnt+=nums[r]

            while cnt>=target:
                ml=min(ml,r-l+1)
                cnt-=nums[l]
                l+=1
        return 0 if ml == float('inf') else ml
        