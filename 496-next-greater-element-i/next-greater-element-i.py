#  class Solution(object):
#     def nextGreaterElement(self, nums, ans):
#         n=len(nums)
#         ans=[-1]*n
#         for i in range(n-1,-1,-1):
#             while len(ans)!=0 and ans[-1]<nums[i]:
#               ans.pop()
#             if len(ans)!=0:
#                ans[i]=nums[i]
#            ans.append(nums[i])
#         return nums


# FOR SINGLE ARRAY 

# class Solution(object):

#     def nextGreaterElement(self, nums, ans):
#         n=len(nums1)
#         ans=[-1]*n

#         for i in range(0,n):
#             for j in range(i+1,n):
#                 if nums[j]>nums[i]:
#                     ans[i]=nums[j]
#                     break
#         return ans


# WHAT THE QUESTION ASKS  -optimal approach

# class Solution(object):
#     def nextGreaterElement(self,nums1,nums2):
#         stack=[]
#         mp={}

#         for i in range(len(nums2)-1,-1,-1):
#             while stack and stack[-1]<nums2[i]:
#                 stack.pop()

#             if stack:
#                 mp[nums2[i]]=stack[-1]
                
#             else:
#                 mp[nums2[i]]=-1

#             stack.append(nums2[i])

#         ans=[]

#         for nums in nums1:
#             ans.append(mp[nums])
            
#         return ans



# BRUTE FORCE APPROACH


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in range(len(nums1)):

            # Find nums1[i] in nums2
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    break

            # Search to the right for the next greater element
            nextGreater = -1
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums1[i]:
                    nextGreater = nums2[k]
                    break

            ans.append(nextGreater)

        return ans