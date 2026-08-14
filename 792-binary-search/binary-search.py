# class Solution(object):
#     def search(self, nums, target):
        # LINEAR SEARCH
    #    for i in range(len(nums)):
    #     if nums[i]==target:
    #         return i
    
    #    return-1




#  BY BINARY SEARCH
class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                #right
                l=mid+1
            else:
                r=mid-1

        return -1

