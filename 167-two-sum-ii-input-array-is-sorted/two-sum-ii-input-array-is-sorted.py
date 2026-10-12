class Solution(object):
    def twoSum(self, nums, target):
        i, j = 0, len(nums)-1

        while j>i:
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                return (i+1,j+1)

