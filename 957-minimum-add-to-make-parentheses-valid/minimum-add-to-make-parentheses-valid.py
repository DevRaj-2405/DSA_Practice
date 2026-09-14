class Solution(object):
    def minAddToMakeValid(self, s):
        stack=[]
        count=0

        for c in s:
            if (c==')'):
                if (not stack or stack[-1] != '('):
                    count+=1
                else:
                    stack.pop()
            else:
                stack.append('(')
        return len(stack) + count

        