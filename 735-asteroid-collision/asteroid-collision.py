# class Solution(object):
#     def asteroidCollision(self, asteroids,n):
#         stack=[]
#         for i in range(0,n):
#             if nums[i]>0:
#                 stack.append(nums[i])
#             else:
#                 while len(stack)!=0 and st[-1]>0 and st[-1]<abs(nums[i]):
#                     st.pop()
#                 if len(stack)!=0 and st[-1]==abs(nums[i]):
#                     st.pop()
#                 elif lem(stack)==0 or st[-1]<0:
#                     st.append(nums[i])
#         return stack




class Solution(object):

    def asteroidCollision(self, asteroids):

        stack = []

        for i in range(len(asteroids)):

            if asteroids[i] > 0:
                stack.append(asteroids[i])

            else:
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()

                if len(stack) != 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()

                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])

        return stack



        # From Code and Debug